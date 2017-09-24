from rest_framework import serializers
from . import models


class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		extra_kwargs = {
			'email': {'write_only': True}
		}
		fields = (
			'id',
			'product',
			'email',
			'review',
			'rating',
			'created_at'
			)
		model = models.Review


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'title',
			'url'
			)
		model = models.Product
