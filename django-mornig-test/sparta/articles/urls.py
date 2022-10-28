from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ArticleAPIView.as_view()),
]