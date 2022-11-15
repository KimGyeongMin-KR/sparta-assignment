from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.ArticleAPIView.as_view(), name="article_list"),
    path('feed/', views.FeedView.as_view()),
    path('<int:article_id>/', views.ArticleDetailAPIView.as_view(), name = "article_detail"),
    path('<int:article_id>/comment/', views.CommentAPIView.as_view(), name = "article_commnet"),
    path('<int:article_id>/comment/<int:comment_id>', views.CommentDetailAPIView.as_view(), name = "article_detail"), 
    path('<int:article_id>/like/', views.LikeView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)