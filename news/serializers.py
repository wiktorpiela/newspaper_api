from rest_framework import serializers
from news.models import Article
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'pub_date', 'author')
        read_only_fields = ('author',)

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)
    email = serializers.EmailField(required=False, validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "articles",)
        extra_kwargs = {
            "password": {"write_only":True},
        }