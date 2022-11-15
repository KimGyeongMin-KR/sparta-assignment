from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Article, Comment
from .serializers import ArticleDetailSerializer, ArticleSerializer, CommentSerializer


class ArticleAPIView(APIView): # c r

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(author = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView): # r, u, d

    def get(self, request, article_id):
        article = get_object_or_404(Article, pk = article_id)
        print(article)
        serializer = ArticleDetailSerializer(article)
        print(serializer)
        return Response(serializer.data)

    def put(self, request, article_id):
        article = get_object_or_404(Article, pk = article_id)
        serializer = ArticleSerializer(article, data = request.data)
        if request.user == article.author:
            if serializer.is_valid():
                serializer.save(author = request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, article_id):
        article = get_object_or_404(Article, pk = article_id)
        if request.user == article.author:
            article.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followings = request.user.followings.all()
        q_objects = Q() # Create an empty Q object to start with
        for person in followings:
            q_objects |= Q(author=person) # 'or' the Q objects together
        print(q_objects)
        articles = Article.objects.filter(q_objects)
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)



class CommentAPIView(APIView): # r u d

    def post(self, request, article_id):
        article = get_object_or_404(Article, pk = article_id)
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(article = article, author = request.user)

        return Response(status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView): # c
    
    def put(self, request, article_id, comment_id): # put의 경우 모든 데이터가 있어야하는데 comment의 기존 데이터와 바꾸는 데이터 request.data가 왔기 때문에 모두 채워진 것?
        comment = get_object_or_404(Comment, pk = comment_id)

        if comment.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, pk = comment_id)
        


class LikeView(APIView):
    def post(self, request, article_id):
        user = request.user
        article = get_object_or_404(Article, pk = article_id)
        if user in article.like.all():
            article.like.remove(user)
            return Response("좋아요 해제",status=status.HTTP_200_OK)
        else:
            article.like.add(user)
            return Response("좋아요",status = status.HTTP_200_OK)