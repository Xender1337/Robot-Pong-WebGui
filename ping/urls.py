__author__ = 'Xender'

from django.conf.urls import patterns, url

from ping import views

urlpatterns = patterns('',
    url(r'^$', views.test, name='test'),
    url(r'^test$', 'test'),
)