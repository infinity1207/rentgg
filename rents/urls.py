from django.conf.urls import url
from rest_framework import routers

from . import views

app_name = 'rents'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^change/(?P<rent_id>[0-9]+)/$', views.change, name='change'),
]

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)