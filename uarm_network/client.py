#!/usr/bin/python

import socket               
import sys

s = socket.socket()        
host = '192.168.0.27' # ip of raspberry pi 
port = 12345
command = sys.argv[1]
s.connect((host, port))
s.sendall(command)
print(s.recv(1024))
s.close()

