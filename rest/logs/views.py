from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.
from logs.gRPC.client import main


class EchoView(APIView):
	permission_classes = (permissions.AllowAny,)

	def get(self, request):

		# log
		history = main( {'ip': 'localhost', 'port': 8888} )

		return Response(data={ 'history': history[:] }, status=201)