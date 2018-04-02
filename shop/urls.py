from django.conf.urls import url
from . import views

app_name='shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/checkout/$', views.checkout, name='checkout'),
]
