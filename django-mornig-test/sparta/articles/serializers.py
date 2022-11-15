from rest_framework import serializers
from articles.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'content']
        read_only_fields = ['author', 'article'] # author과 article은 save()인자에 넣어주면 됨


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField() 

    def get_author(self, obj):
        return obj.author.email
    class Meta:
        model = Article
        fields = '__all__'

class ArticleDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many = True)
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.like.count()

    class Meta:
        model = Article
        fields = ['id', 'content', 'title', 'comment_set', 'like_count']

