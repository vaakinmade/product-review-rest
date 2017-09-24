from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=255)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.title


class Review(models.Model):
	product = models.ForeignKey(Product, related_name="reviews")
	name = models.CharField(max_length=255)
	email = models.EmailField()
	comment = models.TextField(blank=True, default="")
	rating = models.IntegerField()
