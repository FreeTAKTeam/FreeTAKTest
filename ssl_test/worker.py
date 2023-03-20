import selectors
import socket
import ssl
import uuid
import select
import logging
import time
import random
import xml.etree.ElementTree as ET
import threading

from typing import List

from cot_manager import CoTManager
from connection import Connection

class SSLTestWorker:
    """class responsible for creating a test worker which establishes
    and maintains a several connections with the server being tested."""

    def __init__(self, total_connections, dropped_connection_count, terminate, failed_connections, client_id, active_connections, shutdown, connection_count=10):
        
        self.shutdown = shutdown

        self.total_connections = total_connections
        self.dropped_connection_count = dropped_connection_count
        self.terminate = terminate
        self.failed_connections = failed_connections
        self.active_connections = active_connections

        self.client_id = client_id
        self.connection_count = 50

        self.cot_mgmt = CoTManager(client_id, uuid.uuid4())

        self.connections: List[socket.socket] = []

        self.unwrapped_connections: List[socket.socket] = []

    def build_selector(self):
        """build out the selector for use in the main loop"""
        self.selector = selectors.DefaultSelector()
        self.events = selectors.EVENT_READ | selectors.EVENT_WRITE

    def handle_disconnect(self, disconnect_connection: Connection):
        logging.debug("disconnecting socket")
        if disconnect_connection in self.connections:
            self.dropped_connection_count.value += 1
            self.active_connections.value -= 1
            self.connections.remove(disconnect_connection)
            self.selector.unregister(disconnect_connection.ssl_sock)
            disconnect_connection.disconnect()
        else:
            logging.debug("socket already disconnected")
            
    def handle_read(self, selector_key):
        """handling readable sockets"""
        readable_sock = selector_key.fileobj
        readable_connection = selector_key.data
        try:
            readable_sock.settimeout(5)
            con_data = readable_sock.recv(10000)
        except socket.timeout:
            logging.warning("timed out trying to receive data from server")

        if con_data==b"":
            logging.error("client was disconnected")
            self.handle_disconnect(readable_connection)
        
        logging.debug("received data from server"+con_data.decode())

    def handle_write(self, selector_key):
        """this method is responsible for handling the writeable sockets"""
        writable_sock = selector_key.fileobj
        writable_connection = selector_key.data
        msg_obj = self.cot_mgmt.get_message()
        msg = ET.tostring(msg_obj)

        try:
            logging.debug("sent message to server: "+str(msg))
            writable_sock.send(msg)
        except Exception as ex:
            self.handle_disconnect(writable_connection)
            logging.error("sending standard data to ssl service failed "+str(ex))

    def worker_main_loop(self):
        """main worker loop"""
        logging.info("executing main loop")
        while not self.terminate.is_set() and not self.shutdown.is_set() and len(self.connections)>0:
           
            events = self.selector.select()
            if events:
                for key, mask in events:
                    if mask & selectors.EVENT_READ:
                        self.handle_read(key)

                    if mask & selectors.EVENT_WRITE:
                        self.handle_write(key)

                time.sleep(random.randint(1,5))
        logging.info("main loop execution terminated, \nterminate set: "+str(self.terminate.is_set())+"\nshutdown set: "+str(self.shutdown.is_set())+"\nconnection count: "+str(len(self.connections)))

    def cleanup(self):
        """cleanup all connections"""
        logging.info("cleaning up connections")
        for connection in self.connections:
            connection.close()
            self.active_connections.value -= len(self.connections)
    
    def begin_worker(self): 
        """begin the worker process"""
        try:
            logging.info("beggining worker "+str(self.client_id))
            self.build_selector()
            
            self.establish_connections()

            self.worker_main_loop()

            logging.info("worker "+str(self.client_id)+" finished")
        except Exception as e:
            logging.exception("uncaught exception thrown by client "+str(e))
            
            self.dropped_connection_count.value+=len(self.connections)
        
            self.active_connections.value -= len(self.connections)
            return

    def establish_connections(self):
        logging.info("establishing connections")
        for conn_id in range(self.connection_count):
            try:
                connection = Connection(conn_id)
                connection.establish_connection()
                self.connections.append(connection)
            except Exception as e:
                logging.exception("uncaught exception in establishing connection "+str(e))
                self.failed_connections.value += 1
                continue
                
            self.selector.register(connection.ssl_sock, self.events, data=connection)
            self.total_connections.value += 1
            self.active_connections.value += 1
        logging.info("finished establishing connections")