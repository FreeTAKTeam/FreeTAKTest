import socket
import ssl
from typing import List
import xml.etree.ElementTree as ET
import uuid
import random

import time
import multiprocessing
import threading
import logging
import curses
import os

from cot_manager import CoTManager 
from worker import SSLTestWorker

# Configure logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='app_debug.log',
)



#TODO live view of number of clients

#TODO remove worker count

#TODO add failed attempts overall

#TODO add sucessfull attempts overall

#TODO add connection attempts overall

#TODO add number of successfull connection attempts/connection attempts

TEST_FREQUENCY = 30

REFRESH_RATE = 2

STARTING = "Starting"

TESTING = "Testing"

KILLING = "Shuting Down"

ADDRESS = "198.199.70.185"

PORT = 8089

KEY_PATH = "/home/natha/Development/work/FreeTAKTest/ssl_test/certs/KING.key"

CERT_PATH = "/home/natha/Development/work/FreeTAKTest/ssl_test/certs/KING.pem"

BATCH_LENGTH = 1000


class SSLTestClass:
    """the main class responsible for the SSL Stress Test program"""
    def __init__(self, num_clients: int, num_batches: int, max_time: int):
        self.num_clients = num_clients
        self.num_batches = num_batches
        self.max_time = max_time

        self.manager = multiprocessing.Manager()

        self.client_count = self.manager.Value('i', 0)
        self.client_count.value = 0

        self.active_connections = self.manager.Value('i', 0)
        self.active_connections.value = 0

        self.total_connections = self.manager.Value('i', 0)
        self.total_connections.value = 0

        self.batch_num = self.manager.Value('i', 0)
        self.batch_num.value = 0

        self.failure_count = self.manager.Value('i', 0)
        self.failure_count.value = 0

        self.terminate = threading.Event()
        self.terminate.clear()

        self.dropped_connection_count = self.manager.Value('i', 0)
        self.dropped_connection_count.value = 0

        self.failed_connections = self.manager.Value('i', 0)
        self.failed_connections.value = 0

        self.batch_phase = "Starting"
    
    def begin_batching(self):
        """this method handles batching many workers at once"""
        procs = []
        
        # start all workers
        self.start_workers(procs)
        
        # wait for workers
        self.batch_phase = TESTING
        kill_count = 0
        #time.sleep(self.num_clients)
        logging.info("waiting "+str(self.num_clients)+"s to begin disconnects")
        time.sleep(BATCH_LENGTH)
        
        # kill workers at random intervels
        self.kill_workers(procs, kill_count)

    def kill_workers(self, procs, kill_count):
        """kill all workers in a batch"""
        self.batch_phase = KILLING
        logging.info("killing phase")
        while kill_count<len(procs) and not self.terminate.is_set():
            proc, killswitch = random.choice(procs)
            logging.debug("killing proc "+str(proc.pid))
            if proc.is_alive():
                time.sleep(random.randint(0, max_time))
                killswitch.set()
                try:
                    proc.join(3)
                except TimeoutError:
                    proc.terminate()
            proc.join()
            self.client_count.value -= 1
            kill_count+=1

    def start_workers(self, procs):
        self.batch_phase = STARTING
        for client_id in range(self.num_clients):
            killswitch = multiprocessing.Event()
            killswitch.clear()
            worker = SSLTestWorker(self.total_connections, self.dropped_connection_count, self.terminate, self.failed_connections, client_id, self.active_connections, killswitch)
            proc = multiprocessing.Process(target=worker.begin_worker,)
            proc.start()
            logging.debug("started client "+str(client_id)+" on proc "+str(proc.pid))
            procs.append((proc, killswitch))
            self.client_count.value += 1
        
    def test_orchestrator(self):
        """entry point for this class activating the connection validator, visualizer 
        and iterating the test batches"""
        visualizer = threading.Thread(target=self.visualize, args=())
        visualizer.start()
        connection_validator = threading.Thread(target=self.connection_validator, args=())
        connection_validator.start()
        for _ in range(num_batches):
            if self.terminate.is_set(): # check if the application should terminate
                break
            self.batch_num.value+=1
            logging.debug("beggining batch: " + str(self.batch_num))
            self.begin_batching()
        self.terminate.set()
        visualizer.join()
        logging.info("connected clients: "+str(self.client_count.value))
        logging.info("batch number: "+str(self.batch_num.value))
        logging.info("total connections attempted: "+str(self.total_connections.value))
        self.save_export()
        return

    def connection_validator(self):
        """ensure that the server has not died"""
        cot_mgmt = CoTManager("test"+"_"+str(uuid.uuid4()), str(uuid.uuid4()), 1000) # instantiate the cot manager
        
        while not self.terminate.is_set() and self.failure_count.value<=5: # continue until test completes or 6 failures in a row are reached
            # attempt to create socket connection
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ssl_sock = ssl.wrap_socket(s,
                                    keyfile=KEY_PATH,
                                    certfile=CERT_PATH)
                ssl_sock.connect((ADDRESS, PORT))
            except Exception:
                
                self.failed_connections.value += 1
                self.failure_count.value+=1
                time.sleep(TEST_FREQUENCY)
                continue # re-attempt socket conn

            self.failure_count.value = 0 # reset failure count
            self.total_connections.value += 1

            con_msg_obj = cot_mgmt.get_con_message()
            con_msg = ET.tostring(con_msg_obj)
            ssl_sock.send(con_msg)

            time.sleep(TEST_FREQUENCY/4)
            ssl_sock.close()
            time.sleep(TEST_FREQUENCY)

        logging.fatal("SERVER DOWN!")
        self.terminate.set()

    def visualize(self):
        """visualize the current recorded metrics and test progress"""
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.timeout(100)
        while not self.terminate.is_set():
            
            total_cons = self.total_connections.value
        
            failed_cons = self.failed_connections.value
        
            dropped_cons = self.dropped_connection_count.value
        
            active_cons = self.active_connections.value

            fail_count = self.failure_count.value

            stdscr.clear()
            stdscr.addstr(0,0,"connected clients: "+str(self.client_count.value))
            stdscr.addstr(1,0,"batch number: "+str(self.batch_num.value))
            stdscr.addstr(2,0,"total connections attempted: "+str(total_cons))
            stdscr.addstr(3,0,"batch phase: "+str(self.batch_phase))
            stdscr.addstr(4,0,"failed connections: "+str(failed_cons))
            stdscr.addstr(5,0,"failed tests: "+str(fail_count))
            stdscr.addstr(6,0,"dropped_connections: "+str(dropped_cons))
            stdscr.addstr(7,0,"active connections: "+str(active_cons))
            stdscr.refresh()
            time.sleep(REFRESH_RATE)
    
    def save_export(self):
        with open("test_results.txt", "w") as f:
            
            total_cons = self.total_connections.value
        
            failed_cons = self.failed_connections.value
        
            dropped_cons = self.dropped_connection_count.value
        
            active_cons = self.active_connections.value
            f.write("total connections attempted: "+str(total_cons)+"\n")
            f.write("failed connections: "+str(failed_cons)+"\n")
            f.write("dropped_connections: "+str(dropped_cons)+"\n")
            f.write("number of workers: "+str(self.num_clients)+"\n")
            f.write("number of batches: "+str(self.num_batches)+"\n")
            f.write("max wait time between disconnections: "+str(self.max_time)+"\n")
            f.write("active connections: "+str(active_cons)+"\n")

if __name__ == "__main__":
    num_clients = 1
    num_batches = 1
    max_time = 5
    ssl_test_class = SSLTestClass(num_clients, num_batches, max_time)
    ssl_test_class.test_orchestrator()
    os.abort()
