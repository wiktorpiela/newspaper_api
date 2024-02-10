from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "text", "pub_date", "author",)
        read_only_fields = ("id", "pub_date", "author")