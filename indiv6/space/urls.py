from django.urls import path
from django.conf.urls import include
from django.contrib import admin

from . import views

urlpatterns = [
    path('db_initialization', views.db_initialization, name='db_initialization'),
    path('post', views.show_all_forms, name='post'),
    path('post/<str:model_name>', views.show_all_forms, name='post'),
    # path('update', views.show_all_update_forms, name='update'),
    path('update/<str:model_name>&<int:id>', views.show_update, name='update'),
    path('', views.show_planets, name='planets'),
    path('tables/', views.show_tables, name='tables'),
]