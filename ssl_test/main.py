import xml.etree.ElementTree as ET
import uuid
from datetime import datetime as dt
import datetime
import random
import socket
import ssl
import time
import multiprocessing
import threading
import logging
import curses
import os 
import select

# Configure logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='app_error.log',
    filemode='w'
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='app_debug.log',
    filemode='w'
)

ADDRESS = "204.48.30.216"

PORT = 8089

DEVICES = ["GOOGLE PIXEL 6", "GOOGLE PIXEL 5", "GOOGLE PIXEL 4", "SAMSUNG S8", "SAMSUNG S7", "SAMSUNG S6"]

TEAMS = ["red", "yellow", "cyan"]

ROLES = ["Team Leader", "Team Member", "Sniper"]

REFRESH_RATE = 0.5

TEST_FREQUENCY = 2

class CoTManager:

    def __init__(self, callsign, uid, timeout):
        self.callsign = callsign
        self.uid = uid
        self.timeout = 10

    def get_fmt_time(self, delta=None):
        if delta == None:
            delta = self.timeout

        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        now = dt.utcnow()
        zulu = now.strftime(DATETIME_FMT)
        td = datetime.timedelta(seconds=delta)
        stale_part = dt.strptime(zulu, DATETIME_FMT) + td
        return stale_part.strftime(DATETIME_FMT)

    def get_con_message(self):
        event = ET.Element("event", {
            'version': "2.0",
            'type': "a-f-G-U-C",
            'uid': str(uuid.uuid4()),
            'how': "m-g",
            'time': self.get_fmt_time(),
            'start': self.get_fmt_time(),
            'stale': self.get_fmt_time(100),
        })

        ET.SubElement(event, "point", {
            'lat': str(random.randint(-89, 89)),
            'lon': str(random.randint(-179, 179)),
            'hae': "9999999.0",
            'ce': "9999999.0",
            'le': "9999999.0",
        })

        detail = ET.SubElement(event, "detail", {})

        ET.SubElement(detail, "__group", {
            "name": random.choice(TEAMS),
            "role": random.choice(ROLES)
        })

        ET.SubElement(detail, "status", {
            'battery': str(random.randint(1, 100))
        })

        ET.SubElement(detail, "takv", {
            'version': f'{random.randint(1,4)}.{random.randint(0,9)}.{random.randint(0,9)}.{random.randint(0,9)} (79017e13)[playstore].1675714487-CIV',
            'platform': 'ATAK-CIV',
            'device': random.choice(DEVICES),
            'os': str(random.randint(1,33))
        })

        ET.SubElement(detail, "track", {
            'course': str(random.randint(1,359)),
            'speed': str(random.randint(0, 100))
        })

        ET.SubElement(detail, "contact",{
            'callsign': self.callsign,
            'endpoint': '*:-1:stcp',
        })

        ET.SubElement(detail, "uid", {
            'Droid': self.callsign
        })

        ET.SubElement(detail, "precisionlocation", {
            'altsrc': "???"
        })
        return event

    def get_message(self, message_name = str(uuid.uuid1())):
        event = ET.Element("event", {
            'version': "2.0",
            'type': "a-u-G",
            'uid': str(uuid.uuid4()),
            'how': "m-g",
            'time': self.get_fmt_time(),
            'start': self.get_fmt_time(),
            'stale': self.get_fmt_time(),
        })

        ET.SubElement(event, "point", {
            'lat': str(random.randint(-89, 89)),
            'lon': str(random.randint(-179, 179)),
            'hae': "9999999.0",
            'ce': "9999999.0",
            'le': "9999999.0",
        })
        
        detail = ET.SubElement(event, "detail", {})

        ET.SubElement(detail, "status", {
            'readiness': "true"
        })

        ET.SubElement(detail, "archive")

        ET.SubElement(detail, "link", {
            'uid': str(self.callsign),
            'production_time': self.get_fmt_time(),
            'type': "a-f-G-U-C",
            'parent_callsign': self.uid,
            'relation': "p-p",
        })

        ET.SubElement(detail, "contact", {
            'callsign': str(self.callsign)
        })
        
        ET.SubElement(detail, "remarks")

        ET.SubElement(detail, "color", {
            'argb': "-1"
        })

        ET.SubElement(detail, "precisionlocation", {
            'altsrc': "???"
        })

        ET.SubElement(detail, "usericon", {
            'iconsetpath': "COT_MAPPING_2525B/a-u/a-u-G"
        })

        return event
class SSLTestClass:

    def __init__(self, num_clients: int, num_batches: int, max_time: int):
        self.num_clients = num_clients
        self.num_batches = num_batches
        self.max_time = max_time

        self.client_count = multiprocessing.Value('i')
        self.client_count.value = 0

        self.total_connections = multiprocessing.Value('i')
        self.total_connections.value = 0

        self.batch_num = multiprocessing.Value('i')
        self.batch_num.value = 0

        self.terminate = threading.Event()
        self.terminate.clear()

        self.failed_connections = multiprocessing.Value('i')
        self.failed_connections.value = 0

    def create_sock(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(s,
                            keyfile="TestSSL.key",
                            certfile="TestSSL.pem")
        ssl_sock.connect((ADDRESS, PORT))
        return ssl_sock

    def test_client(self, connection_failures, client_id = 0, conn_count = 10):
        socks = []
        for conn_id in range(conn_count):
            try:
                ssl_sock = self.create_sock()
            except Exception as ex:
                connection_failures.value += 1
                logging.error("connection to ssl service failed "+str(ex))
            self.total_connections.value += 1
            cot_mgmt = CoTManager(str(conn_id)+"_"+str(client_id), str(uuid.uuid4()), 1000)
            con_msg_obj = cot_mgmt.get_con_message()
            con_msg = ET.tostring(con_msg_obj)

            try:
                ssl_sock.send(con_msg)
            except Exception as ex:
                logging.error("sending connection data to ssl service failed "+str(ex))

            socks.append(ssl_sock)
        while not self.terminate.is_set():
            ready_to_read, ready_to_write, _ = select.select(socks, socks, [])
            for ready_socket in ready_to_read:
                try:
                    ready_socket.settimeout(5)
                    con_data = ready_socket.recv(10000)
                    logging.debug("received data from server"+con_data.decode())
                except socket.timeout:
                    logging.error("failed to receive from server")
            for ready_socket in ready_to_write:
                msg_obj = cot_mgmt.get_message()
                msg = ET.tostring(msg_obj)
                try:
                    ready_socket.send(msg)
                except Exception as ex:
                    logging.error("sending standard data to ssl service failed "+str(ex))
                time.sleep(random.randint(1,5))

    def test_batch_controller(self):
        procs = []
        for client_id in range(self.num_clients):
            proc = multiprocessing.Process(target=self.test_client, args=(client_id,))
            logging.debug("starting client "+str(client_id)+" on proc "+str(proc.pid))
            proc.start()
            procs.append(proc)
            self.client_count.value += 1
        
        kill_count = 0
        time.sleep(num_clients)
        
        while kill_count<len(procs) and not self.terminate.is_set():
            proc = random.choice(procs)
            logging.debug("killing proc "+str(proc.pid))
            if proc.is_alive():
                time.sleep(random.randint(0, max_time))
                proc.terminate()
            proc.join()
            self.client_count.value -= 1
            kill_count+=1
        
    def test_orchestrator(self):
        visualizer = threading.Thread(target=self.visualize, args=())
        visualizer.start()
        connection_validator = threading.Thread(target=self.connection_validator, args=())
        connection_validator.start()
        for _ in range(num_batches):
            if self.terminate.is_set(): # check if the application should terminate
                break
            self.batch_num.value+=1
            logging.debug("beggining batch: " + str(self.batch_num))
            self.test_batch_controller()
        self.terminate.set()
        visualizer.join()
        logging.info("connected clients: "+str(self.client_count.value))
        logging.info("batch number: "+str(self.batch_num.value))
        logging.info("total connections attempted: "+str(self.total_connections.value))
        return

    def connection_validator(self):
        failure_count = 0 # set the failure counter to 0
        cot_mgmt = CoTManager("test"+"_"+str(uuid.uuid4()), str(uuid.uuid4()), 1000) # instantiate the cot manager
        while not self.terminate.is_set() and failure_count<=5: # continue until test completes or 6 failures in a row are reached
            # attempt to create socket connection
            try:
                ssl_sock = self.create_sock() # attempt to connect to the socket
            except Exception:
                failure_count+=1
                time.sleep(TEST_FREQUENCY)
                continue # re-attempt socket conn
            failure_count = 0 # reset failure count
            self.total_connections.value += 1
            con_msg_obj = cot_mgmt.get_con_message()
            con_msg = ET.tostring(con_msg_obj)
            ssl_sock.send(con_msg)
            time.sleep(TEST_FREQUENCY/4)
            ssl_sock.close()
            time.sleep(TEST_FREQUENCY)
        logging.fatal(" SERVER DOWN!")
        self.terminate.set()

    def visualize(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.timeout(100)
        while not self.terminate.is_set():
            stdscr.clear()
            stdscr.addstr(0,0,"connected clients: "+str(self.client_count.value))
            stdscr.addstr(1,0,"batch number: "+str(self.batch_num.value))
            stdscr.addstr(2,0,"total connections attempted: "+str(self.total_connections.value))
            stdscr.refresh()
            time.sleep(REFRESH_RATE)

if __name__ == "__main__":
    num_clients = 75
    num_batches = 3
    max_time = 5
    ssl_test_class = SSLTestClass(num_clients, num_batches, max_time)
    ssl_test_class.test_orchestrator()
    os.abort()
import xml.etree.ElementTree as ET
import uuid
from datetime import datetime as dt
import datetime
import random
import socket
import ssl
import time
import multiprocessing
import threading
import logging
import curses
import os 
import select

# Configure logger
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='app_error.log',
    filemode='w'
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='app_debug.log',
    filemode='w'
)

ADDRESS = "204.48.30.216"

PORT = 8089

DEVICES = ["GOOGLE PIXEL 6", "GOOGLE PIXEL 5", "GOOGLE PIXEL 4", "SAMSUNG S8", "SAMSUNG S7", "SAMSUNG S6"]

TEAMS = ["red", "yellow", "cyan"]

ROLES = ["Team Leader", "Team Member", "Sniper"]

REFRESH_RATE = 0.5

TEST_FREQUENCY = 2

class CoTManager:

    def __init__(self, callsign, uid, timeout):
        self.callsign = callsign
        self.uid = uid
        self.timeout = 10

    def get_fmt_time(self, delta=None):
        if delta == None:
            delta = self.timeout

        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        now = dt.utcnow()
        zulu = now.strftime(DATETIME_FMT)
        td = datetime.timedelta(seconds=delta)
        stale_part = dt.strptime(zulu, DATETIME_FMT) + td
        return stale_part.strftime(DATETIME_FMT)

    def get_con_message(self):
        event = ET.Element("event", {
            'version': "2.0",
            'type': "a-f-G-U-C",
            'uid': str(uuid.uuid4()),
            'how': "m-g",
            'time': self.get_fmt_time(),
            'start': self.get_fmt_time(),
            'stale': self.get_fmt_time(100),
        })

        ET.SubElement(event, "point", {
            'lat': str(random.randint(-89, 89)),
            'lon': str(random.randint(-179, 179)),
            'hae': "9999999.0",
            'ce': "9999999.0",
            'le': "9999999.0",
        })

        detail = ET.SubElement(event, "detail", {})

        ET.SubElement(detail, "__group", {
            "name": random.choice(TEAMS),
            "role": random.choice(ROLES)
        })

        ET.SubElement(detail, "status", {
            'battery': str(random.randint(1, 100))
        })

        ET.SubElement(detail, "takv", {
            'version': f'{random.randint(1,4)}.{random.randint(0,9)}.{random.randint(0,9)}.{random.randint(0,9)} (79017e13)[playstore].1675714487-CIV',
            'platform': 'ATAK-CIV',
            'device': random.choice(DEVICES),
            'os': str(random.randint(1,33))
        })

        ET.SubElement(detail, "track", {
            'course': str(random.randint(1,359)),
            'speed': str(random.randint(0, 100))
        })

        ET.SubElement(detail, "contact",{
            'callsign': self.callsign,
            'endpoint': '*:-1:stcp',
        })

        ET.SubElement(detail, "uid", {
            'Droid': self.callsign
        })

        ET.SubElement(detail, "precisionlocation", {
            'altsrc': "???"
        })
        return event

    def get_message(self, message_name = str(uuid.uuid1())):
        event = ET.Element("event", {
            'version': "2.0",
            'type': "a-u-G",
            'uid': str(uuid.uuid4()),
            'how': "m-g",
            'time': self.get_fmt_time(),
            'start': self.get_fmt_time(),
            'stale': self.get_fmt_time(),
        })

        ET.SubElement(event, "point", {
            'lat': str(random.randint(-89, 89)),
            'lon': str(random.randint(-179, 179)),
            'hae': "9999999.0",
            'ce': "9999999.0",
            'le': "9999999.0",
        })
        
        detail = ET.SubElement(event, "detail", {})

        ET.SubElement(detail, "status", {
            'readiness': "true"
        })

        ET.SubElement(detail, "archive")

        ET.SubElement(detail, "link", {
            'uid': str(self.callsign),
            'production_time': self.get_fmt_time(),
            'type': "a-f-G-U-C",
            'parent_callsign': self.uid,
            'relation': "p-p",
        })

        ET.SubElement(detail, "contact", {
            'callsign': str(self.callsign)
        })
        
        ET.SubElement(detail, "remarks")

        ET.SubElement(detail, "color", {
            'argb': "-1"
        })

        ET.SubElement(detail, "precisionlocation", {
            'altsrc': "???"
        })

        ET.SubElement(detail, "usericon", {
            'iconsetpath': "COT_MAPPING_2525B/a-u/a-u-G"
        })

        return event
class SSLTestClass:

    def __init__(self, num_clients: int, num_batches: int, max_time: int):
        self.num_clients = num_clients
        self.num_batches = num_batches
        self.max_time = max_time

        self.client_count = multiprocessing.Value('i')
        self.client_count.value = 0

        self.total_connections = multiprocessing.Value('i')
        self.total_connections.value = 0

        self.batch_num = multiprocessing.Value('i')
        self.batch_num.value = 0

        self.terminate = threading.Event()
        self.terminate.clear()

        self.failed_connections = multiprocessing.Value('i')
        self.failed_connections.value = 0

    def create_sock(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(s,
                            keyfile="TestSSL.key",
                            certfile="TestSSL.pem")
        ssl_sock.connect((ADDRESS, PORT))
        return ssl_sock

    def test_client(self, connection_failures, client_id = 0, conn_count = 10):
        socks = []
        for conn_id in range(conn_count):
            try:
                ssl_sock = self.create_sock()
            except Exception as ex:
                connection_failures.value += 1
                logging.error("connection to ssl service failed "+str(ex))
            self.total_connections.value += 1
            cot_mgmt = CoTManager(str(conn_id)+"_"+str(client_id), str(uuid.uuid4()), 1000)
            con_msg_obj = cot_mgmt.get_con_message()
            con_msg = ET.tostring(con_msg_obj)

            try:
                ssl_sock.send(con_msg)
            except Exception as ex:
                logging.error("sending connection data to ssl service failed "+str(ex))

            socks.append(ssl_sock)
        while not self.terminate.is_set():
            ready_to_read, ready_to_write, _ = select.select(socks, socks, [])
            for ready_socket in ready_to_read:
                try:
                    ready_socket.settimeout(5)
                    con_data = ready_socket.recv(10000)
                    logging.debug("received data from server"+con_data.decode())
                except socket.timeout:
                    logging.error("failed to receive from server")
            for ready_socket in ready_to_write:
                msg_obj = cot_mgmt.get_message()
                msg = ET.tostring(msg_obj)
                try:
                    ready_socket.send(msg)
                except Exception as ex:
                    logging.error("sending standard data to ssl service failed "+str(ex))
                time.sleep(random.randint(1,5))

    def test_batch_controller(self):
        procs = []
        for client_id in range(self.num_clients):
            proc = multiprocessing.Process(target=self.test_client, args=(client_id,))
            logging.debug("starting client "+str(client_id)+" on proc "+str(proc.pid))
            proc.start()
            procs.append(proc)
            self.client_count.value += 1
        
        kill_count = 0
        time.sleep(num_clients)
        
        while kill_count<len(procs) and not self.terminate.is_set():
            proc = random.choice(procs)
            logging.debug("killing proc "+str(proc.pid))
            if proc.is_alive():
                time.sleep(random.randint(0, max_time))
                proc.terminate()
            proc.join()
            self.client_count.value -= 1
            kill_count+=1
        
    def test_orchestrator(self):
        visualizer = threading.Thread(target=self.visualize, args=())
        visualizer.start()
        connection_validator = threading.Thread(target=self.connection_validator, args=())
        connection_validator.start()
        for _ in range(num_batches):
            if self.terminate.is_set(): # check if the application should terminate
                break
            self.batch_num.value+=1
            logging.debug("beggining batch: " + str(self.batch_num))
            self.test_batch_controller()
        self.terminate.set()
        visualizer.join()
        logging.info("connected clients: "+str(self.client_count.value))
        logging.info("batch number: "+str(self.batch_num.value))
        logging.info("total connections attempted: "+str(self.total_connections.value))
        return

    def connection_validator(self):
        failure_count = 0 # set the failure counter to 0
        cot_mgmt = CoTManager("test"+"_"+str(uuid.uuid4()), str(uuid.uuid4()), 1000) # instantiate the cot manager
        while not self.terminate.is_set() and failure_count<=5: # continue until test completes or 6 failures in a row are reached
            # attempt to create socket connection
            try:
                ssl_sock = self.create_sock() # attempt to connect to the socket
            except Exception:
                failure_count+=1
                time.sleep(TEST_FREQUENCY)
                continue # re-attempt socket conn
            failure_count = 0 # reset failure count
            self.total_connections.value += 1
            con_msg_obj = cot_mgmt.get_con_message()
            con_msg = ET.tostring(con_msg_obj)
            ssl_sock.send(con_msg)
            time.sleep(TEST_FREQUENCY/4)
            ssl_sock.close()
            time.sleep(TEST_FREQUENCY)
        logging.fatal(" SERVER DOWN!")
        self.terminate.set()

    def visualize(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.timeout(100)
        while not self.terminate.is_set():
            stdscr.clear()
            stdscr.addstr(0,0,"connected clients: "+str(self.client_count.value))
            stdscr.addstr(1,0,"batch number: "+str(self.batch_num.value))
            stdscr.addstr(2,0,"total connections attempted: "+str(self.total_connections.value))
            stdscr.refresh()
            time.sleep(REFRESH_RATE)

if __name__ == "__main__":
    num_clients = 75
    num_batches = 3
    max_time = 5
    ssl_test_class = SSLTestClass(num_clients, num_batches, max_time)
    ssl_test_class.test_orchestrator()
    os.abort()
