import traceback
from server_build import cl_wrapper

__author__ = 'Valera'

import socket
import pickle

while True:
    try:
        print('start')
        soc = socket.socket()
        soc.bind(('', 8080))
        soc.listen(1)
        conn, addr = soc.accept()

        in_data = b''
        while True:
            # print(pickle.loads(conn.recv(1024)))
            b = conn.recv(1024)
            if not b:
                break
            else:
                in_data += b

        data, wp = pickle.loads(in_data)
        impl_wp = cl_wrapper.Wrapper()
        impl_wp.row, impl_wp.column, impl_wp.depth_value, impl_wp.trace_time, impl_wp.label = wp

        print('data load')
        conn, addr = soc.accept()

        print(conn, addr)
        conn.close()
        soc.close()
        print('close')
    except Exception:
        print(traceback.print_exc())
        soc.close()
        conn.close()