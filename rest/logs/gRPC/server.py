import os
import os.path as osp
import sys
import threading
from mqtt.subscriber import record, getHistory

BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
from concurrent import futures
import log_pb2
import log_pb2_grpc


sub = threading.Thread(target=record)

class LogProviderServicer(log_pb2_grpc.LogProviderServicer):

	def __init__(self):
		pass

	def Show(self, request, context):

		response = log_pb2.LogResponse()
		response.history.extend(getHistory())

		return response

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", default="0.0.0.0", type=str)
	parser.add_argument("--port", default=8888, type=int)
	args = vars(parser.parse_args())

	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	servicer = LogProviderServicer()
	log_pb2_grpc.add_LogProviderServicer_to_server(servicer, server)

	sub.start()
	print( "sub started" )

	try:
		server.add_insecure_port(f"{args['ip']}:{args['port']}")
		server.start()
		print(f"Run gRPC Server at {args['ip']}:{args['port']}")
		server.wait_for_termination()

	except KeyboardInterrupt:
		pass
