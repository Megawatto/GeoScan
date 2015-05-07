__author__ = 'Valera'

import socket
import pickle

print('start')
soc = socket.socket()
soc.bind(('', 8080))
soc.listen(1)
conn, addr = soc.accept()
data = b''
while True:
    # print(pickle.loads(conn.recv(1024)))
    b = conn.recv(1024)
    if not b:
        break
    else:
        data += b
data = pickle.loads(data)
print(data)
print(conn, addr)
conn.close()
soc.close()
print('close')
