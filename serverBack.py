#!/usr/bin/env python3
import socket
 
def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            break
        c.send(data)
    c.close()
 
host = "0.0.0.0"
port = 2222
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
while True:
    sock, addr = s.accept()
    print('Connected to :', addr[0], ':', addr[1])
    start_new_thread(threaded, (sock,))
