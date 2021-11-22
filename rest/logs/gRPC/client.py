import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
import log_pb2
import log_pb2_grpc


def main(args):
	host = f"{args['ip']}:{args['port']}"
	print(host)
	with grpc.insecure_channel(host) as channel:
		stub = log_pb2_grpc.LogProviderStub(channel)

		request = log_pb2.LogRequest()

		response = stub.Show(request)
		return response.history


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default="localhost")
	parser.add_argument("--port", type=int, default=8888)
	args = vars(parser.parse_args())
	main(args)
