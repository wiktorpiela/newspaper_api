from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'pub_date', 'author')
        read_only_fields = ('author',)