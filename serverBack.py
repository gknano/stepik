#!/usr/bin/env python
 
import socket
 
serverBack = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverBack.bind(('0.0.0.0', 2222))
serverBack.listen(10)
client, addr = serverBack.accept()
while True:
    data = client.recv(1024)
    if len(data) > 1024 or data == 'close':
        client.close()
        break
    else:
        client.send(data)
        print data
    serverBack.close()