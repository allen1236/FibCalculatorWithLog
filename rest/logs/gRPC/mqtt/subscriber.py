import time
import argparse

import psutil
import paho.mqtt.client as mqtt

import threading
history = []



def on_message(client, obj, msg):
	print(f"new {msg.topic}: {int(msg.payload)}")
	history.append( int(msg.payload) )

def getHistory():
	return history


def record():

	print("record started")
	client = mqtt.Client()
	client.on_message = on_message
	client.connect(host="localhost", port=1883)
	client.subscribe('history', 0)

	try:
		client.loop_forever()
	except KeyboardInterrupt as e:
		pass




def main(args):
	# Establish connection to mqtt broker
	client = mqtt.Client()
	client.on_message = on_message
	client.connect(host=args['ip'], port=args['port'])
	client.subscribe('cpu', 0)
	client.subscribe('mem', 0)

	try:
		client.loop_forever()
	except KeyboardInterrupt as e:
		pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip",
						default="localhost",
						help="service ip of MQTT broker")
	parser.add_argument("--port",
						default=1883,
						type=int,
						help="service port of MQTT broker")
	args = vars(parser.parse_args())
	record()
