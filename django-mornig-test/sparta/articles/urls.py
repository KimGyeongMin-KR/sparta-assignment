from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
]