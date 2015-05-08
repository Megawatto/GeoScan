import traceback

__author__ = 'Valera'

import pickle
import socket
import client_build.client_img

data_point = []
cluster_zone = []

def request_filter_data(data, wrappers, limit_box, scale):
    try:
        global data_point
        global cluster_zone
        wr = [wrappers.row, wrappers.column, wrappers.trace_time, wrappers.depth_value, wrappers.label]
        soc = socket.socket()
        soc.connect(('localhost', 8080))
        middle_data = [data, wr, limit_box]
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
        data_point, cluster_zone = pickle.loads(data_point)
        print(data_point)
        #fixme потом разделить клиент и графику, пока временно так сойдет
        create_find(data_point, limit_box, scale)
        # create_zona(cluster_zone, scale)
    except Exception:
        print(traceback.print_exc())

def reset_data():
    global cluster_zone
    global data_point
    cluster_zone = []
    data_point = []

def create_img(data, size, scale):
    client_build.client_img.create_img(size[0], size[1], scale)
    client_build.client_img.draw_radarogramms(data, scale)


def create_find(find_point, limit_box, scale):
    client_build.client_img.create_limit(limit_box[0], limit_box[2], limit_box[1], limit_box[3], scale)
    client_build.client_img.draw_point(find_point, scale)
    print('create_filter')


def create_zona(cluster_zona, scale):
    print(cluster_zone)
    for var in cluster_zona:
        client_build.client_img.create_zona(var[0], var[1], var[2], var[3], scale)
    client_build.client_img.show()
