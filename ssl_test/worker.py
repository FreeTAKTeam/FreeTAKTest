import socket
import ssl
import uuid
import select
import logging
import time
import random
import xml.etree.ElementTree as ET

from typing import List

from cot_manager import CoTManager

ADDRESS = "198.199.70.185"

PORT = 8089

KEY_PATH = "ssl_test/certs/Dev.key"

CERT_PATH = "ssl_test/certs/Dev.pem"

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

    def create_sock(self):
        """create and connect socket"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(s,
                            keyfile=KEY_PATH,
                            certfile=CERT_PATH)
        ssl_sock.connect((ADDRESS, PORT))
        return s, ssl_sock
    
    def worker_main_loop(self):
        """main worker loop """
        while not self.terminate.is_set() and not self.shutdown.is_set():
            ready_to_read, ready_to_write, _ = select.select(self.connections, self.connections, [])
            for ready_socket in ready_to_read:
                try:
                    ready_socket.settimeout(5)
                    con_data = ready_socket.recv(10000)
                    
                    if con_data==b"":
                        logging.error("client was disconnected")
                        with self.dropped_connection_count.get_lock():
                            self.dropped_connection_count.value += 1
                        with self.active_connections.get_lock():
                            self.active_connections.value -= 1
                        self.connections.remove(ready_socket)
                        ready_socket.close()
                        continue
                    
                    logging.debug("received data from server"+con_data.decode())

                except socket.timeout:
                    logging.warning("timed out trying to receive data from server")

            for ready_socket in ready_to_write:
                
                msg_obj = self.cot_mgmt.get_message()
                msg = ET.tostring(msg_obj)

                try:
                    ready_socket.send(msg)
                except Exception as ex:
                    with self.dropped_connection_count.get_lock():
                        self.dropped_connection_count.value += 1
                    with self.active_connections.get_lock():
                        self.active_connections.value -= 1
                    logging.error("sending standard data to ssl service failed "+str(ex))
                    return
                
                time.sleep(random.randint(1,5))
    
    def establish_connection(self, conn_id):
        """establish a connection to the TAKServer"""
        try:
            unwrapped_sock, ssl_sock = self.create_sock()
        except Exception as ex:
            with self.failed_connections.get_lock():
                self.failed_connections.value += 1
            logging.error("connection to ssl service failed "+str(ex))
            return None, None

        cot_mgmt = CoTManager(str(conn_id)+"_"+str(self.client_id), str(uuid.uuid4()), 1000)
        con_msg_obj = cot_mgmt.get_con_message()
        con_msg = ET.tostring(con_msg_obj)

        try:
            ssl_sock.send(con_msg)
        except Exception as ex:
            with self.dropped_connection_count.get_lock():
                self.dropped_connection_count.value += 1

            with self.active_connections.get_lock():
                self.active_connections.value -= 1

            logging.error("sending connection data to ssl service failed "+str(ex))
            return None, None
        
        with self.total_connections.get_lock():
            self.total_connections.value += 1

        with self.active_connections.get_lock():
            self.active_connections.value += 1

        return unwrapped_sock, ssl_sock

    def cleanup(self):
        for connection in self.connections:
            connection.close()
        with self.active_connections.get_lock():
            self.active_connections.value -= len(self.connections)

    def begin_worker(self): 
        """begin the worker process"""
        try:
            for conn_id in range(self.connection_count):
                try:
                    unwrapped_sock, ssl_sock = self.establish_connection(conn_id)
                    if ssl_sock != None:
                        self.connections.append(ssl_sock)
                        self.unwrapped_connections.append(unwrapped_sock)
                    else:
                        logging.debug("establish connection failed moving on")
                except Exception as e:
                    logging.exception("uncaught exception in establishing connection "+str(e))

            self.worker_main_loop()

        except Exception as e:
            logging.exception("uncaught exception thrown by client "+str(e))
            with self.dropped_connection_count.get_lock():
                self.dropped_connection_count+=len(self.connections)
            with self.active_connections.get_lock():
                self.active_connections.value -= len(self.connections)
            return
