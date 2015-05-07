import traceback

__author__ = 'Valera'

import pickle
import socket


def create_connect(data, wrappers):
    global soc
    try:
        wr = [wrappers.row, wrappers.column, wrappers.trace_time, wrappers.depth_value, wrappers.label]
        print(wr)
        soc = socket.socket()
        soc.connect(('localhost', 8080))
        middle_data = [data, wr]
        ready_data = pickle.dumps(middle_data)
        soc.send(ready_data)
        soc.close()
    except Exception:
        print(traceback.print_exc())