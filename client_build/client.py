import traceback

__author__ = 'Valera'

import pickle
import socket
import client_build.client_img

def create_connect(data, wrappers, size, scale):
    try:
        wr = [wrappers.row, wrappers.column, wrappers.trace_time, wrappers.depth_value, wrappers.label]
        soc = socket.socket()
        soc.connect(('localhost', 8080))
        middle_data = [data, wr]
        ready_data = pickle.dumps(middle_data)
        soc.sendall(ready_data)
        # soc.close()
        data_point = b''
        while True:
            buff = soc.recv(1024)
            if not buff:
                break
            else:
                data_point += buff
        soc.close()
        data_point = pickle.loads(data_point)
        create_find(data_point, scale)
    except Exception:
        print(traceback.print_exc())


def create_img(data, size, scale):
    client_build.client_img.create_img(size[0], size[1], scale)
    client_build.client_img.draw_radarogramms(data, scale)

def create_find(find_point, scale):
    client_build.client_img.draw_point(find_point, scale)
    print('create_filter')