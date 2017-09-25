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
			'comment',
			'rating',
			'created_at'
			)
		model = models.Review


class ProductSerializer(serializers.ModelSerializer):
	reviews = ReviewSerializer(many=True, read_only=True)
	class Meta:
		fields = (
			'id',
			'title',
			'url',
			'reviews',
			)
		model = models.Product
