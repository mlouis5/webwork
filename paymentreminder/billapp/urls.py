__author__ = 'Mac'

from django.conf.urls import patterns, url
from billapp import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'))
