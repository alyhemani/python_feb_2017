from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^confirm/(?P<id>\d+)$', views.confirm),
]
