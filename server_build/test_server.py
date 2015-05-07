import traceback
from server_build import connector
from server_build import cl_wrapper

__author__ = 'Valera'

import socket
import pickle

while True:
    try:
        print('start')
        soc = socket.socket()
        soc.bind(('', 8080))
        soc.listen(2)
        conn, addr = soc.accept()
        in_data = b''
        conn.settimeout(1)
        try:
            while True:
                b = conn.recv(100000)
                if not b:
                    break
                else:
                    in_data += b
        except socket.timeout:
            print('>>>')
        print('data load')
        data, wp, limit_box = pickle.loads(in_data)
        impl_wp = cl_wrapper.Wrapper()
        impl_wp.row, impl_wp.column, impl_wp.depth_value, impl_wp.trace_time, impl_wp.label = wp
        response = connector.start_filter(data, limit_box, impl_wp)
        response = pickle.dumps(response)
        conn.send(response)

        print('data load')
        print(conn, addr)
        conn.close()
        soc.close()
        print('close')
    except Exception:
        print(traceback.print_exc())
        soc.close()
        conn.close()