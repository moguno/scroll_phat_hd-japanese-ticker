#!/usr/bin/env python3

import time
import datetime
import types
import copy
import signal
import threading
import socket

import scrollphathd
from scrollphathd.fonts import font5x7

import misaki

print("Press Ctrl+C to exit!")

channels = {}

str = time.asctime(time.localtime())

def accept_thread():
	global channels

	serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serversock.bind(("localhost", 39114))
	serversock.listen(10)

	while True:
		client_sock, client_address = serversock.accept()
		msg = client_sock.recv(8192).strip().decode("utf-8")

		data = msg.split("\t")
		channel = data[0]

		print(len(data))

		if len(data) <= 1:
			if channel in channels:
				del channels[channel]
		else:
			message = data[1]
			channels[channel] = message

		client_sock.close()

scrollphathd.set_brightness(0.3)

thread = threading.Thread(target = accept_thread, name = "accept", args = ())
thread.start()

channels["time"] = lambda: datetime.datetime.now().strftime("%m/%d %H:%M")

while True:
	current_channels = copy.copy(channels)

	for channel, message_tmp in current_channels.items():

		if type(message_tmp) is types.LambdaType:
			message = message_tmp()
		else:
			message = message_tmp

		print(message)

		scrollphathd.write_string("　　＊" + message + "                       _", x=0, y=0, font=misaki, brightness=0.5)

		for i in range((len(message) + 6) * misaki.width):
			scrollphathd.show()
			scrollphathd.scroll()
			time.sleep(0.02)

		scrollphathd.clear()
