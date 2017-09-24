from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from . import models
from . import serializers


class ListCreateProduct(generics.ListCreateAPIView):
	queryset = models.Product.objects.all()
	serializer_class = serializers.ProductSerializer


class RetrieveUpdateDestroyProduct(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Product.objects.all()
	serializer_class = serializers.ProductSerializer


class ListCreateReview(generics.ListCreateAPIView):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer

	def get_queryset(self):
		return self.queryset.filter(product_id=self.kwargs.get('product_pk'))

	def perform_create(self, serializer):
		product = get_object_or_404(
			models.Product, pk=self.kwargs.get('product_pk'))
		serializer.save(product=product)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer

	def get_object(self):
		return get_object_or_404(
			self.get_queryset(),
			product_id=self.kwargs.get('product_pk'),
			pk=self.kwargs.get('pk')
		)


class ProductViewSet(viewsets.ModelViewSet):
	queryset = models.Product.objects.all()
	serializer_class = serializers.ProductSerializer

	@detail_route(methods=['get'])
	def reviews(self, request, pk=None):
		product = self.get_object()
		serializer = serializers.ReviewSerializer(
			product.reviews.all(), many=True)
		return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer