from rest_framework import generics

from . import models
from . import serializers


class ListCreateProduct(generics.ListCreateAPIView):
	queryset = models.Product.objects.all()
	serializer_class = serializers.ProductSerializer


class RetrieveUpdateDestroyProduct(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Product.objects.all()
	serializer_class = serializers.ProductSerializer