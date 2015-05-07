__author__ = 'Valera'

import pickle
import socket


def create_connect(data):
    global soc
    ready_data = pickle.dumps(data)
    soc = socket.socket()
    soc.connect(('localhost', 8080))
    soc.send(ready_data)
    soc.close()
