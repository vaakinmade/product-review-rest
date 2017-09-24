from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListCreateProduct.as_view(), name="product_list"),
	url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyProduct.as_view(),
		name='product_detail')
]