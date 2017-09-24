from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListCreateProduct.as_view(), name="product_list"),
	url(r'^(?P<pk>\d+)/$', views.RetrieveUpdateDestroyProduct.as_view(),
		name='product_detail'),
	url(r'^(?P<product_pk>\d+)/reviews/$', views.ListCreateReview.as_view(),
		name='review_list'),
	url(r'^(?P<product_pk>\d+)/reviews/(?P<pk>\d+)/$',
		views.RetrieveUpdateDestroyReview.as_view(),
		name='review_detail'),
]