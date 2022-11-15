from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/', views.UserView.as_view(), name='signup'),
    path('mock/', views.MockView.as_view(), name='mock'),
    path('login/', views.login, name='login'),
    path('follow/<int:user_id>', views.FollowView.as_view(), name='user_follow'),
    path('<int:user_id>/', views.ProfileView.as_view(), name='user_follow'),
]