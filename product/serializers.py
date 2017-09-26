from django.db.models import Avg

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
	reviews = serializers.HyperlinkedRelatedField(
		many=True,
		read_only=True,
		view_name='apiv2:review-detail')
	average_rating = serializers.SerializerMethodField()
	class Meta:
		fields = (
			'id',
			'title',
			'url',
			'reviews',
			'average_rating',
			)
		model = models.Product

	def get_average_rating(self, obj):
		average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')
		if average is None:
			return 0
		return round(average*2) / 2
