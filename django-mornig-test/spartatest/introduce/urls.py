from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'introduce'


urlpatterns = [
    path('', views.index),
]