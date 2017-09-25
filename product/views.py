from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import mixins

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

	# prevent making a review for a different product than the one selected
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
		self.pagination_class.page_size = 1
		reviews = models.Review.objects.filter(product_id=pk)

		page = self.paginate_queryset(reviews)

		if page is not None:
			serializer = serializers.ReviewSerializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = serializers.ReviewSerializer(
			reviews, many=True)
		return Response(serializer.data)


class ReviewViewSet(mixins.CreateModelMixin,
					mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					viewsets.GenericViewSet):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer