from rest_framework import serializers, exceptions
from news.models import Article
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

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

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        email = validated_data.get("email")

        try:
            validate_password(password)
        except ValidationError as e:
            raise exceptions.ValidationError(e)
        else:
            if email:
                user = User.objects.create_user(username=username, email=email, password=password)
            else:
                user = User.objects.create_user(username=username, password=password)
            return user
        
    def update(self, instance, validated_data):
        username = validated_data.get("username")
        email = validated_data.get("email")
        password = validated_data.get("password")

        try:
            validate_password(password)
        except ValidationError as e:
            raise exceptions.ValidationError(e)
        else:
            instance.username = username
            instance.set_password(password)
            if email:
                instance.email = email
            instance.save()
            return instance