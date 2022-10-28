from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/', views.UserView.as_view(), name='signup'),
    path('mock/', views.MockView.as_view(), name=''),
    path('login/', views.login, name='login'),
]