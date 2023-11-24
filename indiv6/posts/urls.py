from django.urls import path
from django.conf.urls import include
from django.contrib import admin

# from .views import {
#
# }

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
]