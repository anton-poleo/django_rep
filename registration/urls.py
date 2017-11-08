from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trader/$', views.register_trader, name='trader'),
    url(r'^index/$', views.reg_test, name='index')
]
