from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import Http404
from django.contrib.auth.password_validation import validate_password

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "text", "date", "author",)
        read_only_fields = ("id", "date",) #te ktorych nie chce dostawac przy wysyłaniu requesta

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all()) #wiele artykułów do modelu usera

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "articles",)

    def create(self, validated_data): #requested data
        username = validated_data.get("username")   
        email = validated_data.get("email")
        password = validated_data.get("password")

        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        else:
            if email:
                emailTaken = User.objects.filter(email=email).exists()
                if not emailTaken:
                    user = User.objects.create(username=username,email=email,password=password)  
                else:
                    raise serializers.ValidationError("This email is already taken.")
            else:
                user = User.objects.create(username=username,password=password)   
            return user
