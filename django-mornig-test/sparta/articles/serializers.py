from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user.id

        print(validated_data)
        
        instance = super().create(validated_data)
        return instance