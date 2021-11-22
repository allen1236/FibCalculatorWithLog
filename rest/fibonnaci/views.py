from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

import json
from fibonnaci.gRPC.client import main
from fibonnaci.mqtt.publisher import send


# Create your views here.


class EchoView(APIView):
	permission_classes = (permissions.AllowAny,)

	def post(self, request):

		# fibonnaci
		order =  json.loads(request.body)['order']

		send(order)
		ans = main( {'ip': 'localhost', 'port': 8080, 'order': order} )

		return Response(data={ 'answer': ans }, status=201)
