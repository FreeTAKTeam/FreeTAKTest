import socket
import ssl
import logging
import uuid

import xml.etree.ElementTree as ET

from cot_manager import CoTManager

KEY_PATH = "/home/natha/Development/work/FreeTAKTest/ssl_test/certs/KING.key"

CERT_PATH = "/home/natha/Development/work/FreeTAKTest/ssl_test/certs/KING.pem"

ADDRESS = "198.199.70.185"

PORT = 8089


class Connection:
    def __init__(self, connection_id) -> None:
        self.connection_id = connection_id
        self.cot_mgmt = CoTManager(connection_id, self.connection_id)
        self.ssl_sock = None
        self.unwrapped_sock = None

    def create_sock(self):
        """create and connect socket"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(s,
                            keyfile=KEY_PATH,
                            certfile=CERT_PATH)
        ssl_sock.connect((ADDRESS, PORT))
        ssl_sock.setblocking(False)
        return s, ssl_sock
    
    def establish_connection(self):
        """establish a connection to the TAKServer"""
        unwrapped_sock, ssl_sock = self.create_sock()
        
        cot_mgmt = CoTManager(str(self.connection_id), str(uuid.uuid4()), 1000)
        con_msg_obj = cot_mgmt.get_con_message()
        con_msg = ET.tostring(con_msg_obj)
        ssl_sock.send(con_msg)
        
        self.ssl_sock = ssl_sock
        self.unwrapped_sock = unwrapped_sock

    def get_sock(self):
        return self.ssl_sock
    
    def get_data(self):
        return self.ssl_sock.recv(1024)
    
    def send_updates(self):
        update_message = self.cot_mgmt.get_message()
        self.ssl_sock.send(update_message)

    def disconnect(self):
        self.ssl_sock.close()
        self.unwrapped_sock.close()