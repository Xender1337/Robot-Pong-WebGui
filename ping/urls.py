__author__ = 'Xender'

from django.conf.urls import patterns, url

from ping import views

urlpatterns = patterns('',
    url(r'^$', views.test, name='test'),
    url(r'^test/$',views.test, name='test'),
    url(r'^ajax_cadence/$',views.ajax_cadence, name='ajax_cadence'),
    url(r'^ajax_vitesse/$',views.ajax_vitesse, name='ajax_vitesse'),
)