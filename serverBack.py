#!/usr/bin/env python
 
import socket
 
serverBack = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverBack.bind(('0.0.0.0', 2222))
serverBack.listen(10)
while True:
	conn, addr = serverBack.accept()
    data = conn.recv(1024)
    if len(data) > 1024 or data == 'close':
        break
    else:
        conn.send(data)
        print data
    serverBack.close()