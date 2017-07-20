import socket
import _thread, threading
import serial
import sys, os
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), '../../pyuf'))

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *

#logger_init(logging.DEBUG)
logger_init(logging.INFO)

print('setup swift ...')

swift = SwiftAPI(dev_port = '/dev/ttyACM0')

print('sleep 2 sec ...')
sleep(2)

print('device info: ')
print(swift.get_device_info())

s = socket.socket()
host = '192.168.0.27' #ip of raspberry pi
port = 12345
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send(bytes('Thank you for connecting','utf-8'))
  c.close()
