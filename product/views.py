from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers


class ListCreateProduct(APIView):
	def get(self, request, format=None):
		products = models.Product.objects.all()
		serializer = serializers.ProductSerializer(products, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = serializers.ProductSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)