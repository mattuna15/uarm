import socket
import _thread, threading
import serial
import sys, os
from time import sleep

sys.path.append(os.path.join(os.path.dirname(__file__), '../../pyuf'))

from uf.wrapper.swift_api import SwiftAPI
from uf.utils.log import *


def str2bool(v):
	return v.lower() in ("yes", "true", "t", "1")

logger_init(logging.DEBUG)

print('setup swift ...')

swift = SwiftAPI(dev_port = '/dev/ttyACM0')

print('sleep 2 sec ...')
sleep(2)

print('device info: ')
print(swift.get_device_info())

sock = socket.socket()
host = '192.168.0.27' #ip of raspberry pi
port = 12345
sock.bind((host, port))
sock.listen(5)
while True:
	print('waiting for a connection')
	connection, client_address = sock.accept()
	try:
		print('client connected: {}'.format(client_address))
		while True:
			data = connection.recv(128).decode()
			print('received {}"'.format(str(data)))
			if data == 'position':
				position = swift.get_position()                
				positionResponse = 'x: {:03.2f}, y: {:03.2f}, z: {:03.2f}'.format(position[0],position[1],position[2])
				print('sending response: {}'.format(str(positionResponse)))
				connection.sendall(bytes(positionResponse,'utf-8'))
			elif data == 'info':
				info = str(swift.get_device_info())
				print('sending response: {}'.format(str(info)))
				connection.sendall(bytes(info,'utf-8'))
			elif data == 'reset':
				swift.reset()
				connection.sendall(bytes('OK','utf-8'))
			elif 'move' in data:
				command = data.split()
				print(str(command))
				new_x = command[1]
				new_y = command[2]
				new_z = command[3]
				speed = command[4]
				moveRelative = str2bool(command[5])
				print('relative: {}'.format(moveRelative))
				swift.set_position(x=float(new_x), y=float(new_y), z=float(new_z), speed=float(speed), relative=moveRelative, wait=False)
				sleep(0.1)
				connection.sendall(bytes('OK','utf-8'))
			else:
				break
	finally:
		connection.close()


