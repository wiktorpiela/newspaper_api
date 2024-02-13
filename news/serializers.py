from rest_framework import serializers, exceptions
from news.models import Article
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Article
        fields = ('id','title', 'text', 'pub_date', 'author')
        read_only_fields = ('author',) #'id', 'pub_date', automatycznie

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "articles",) # pola które widać
        extra_kwargs = {
            "password": {"write_only":True},
        }

    # walidacja czu spełnia warunki 1
    # czy username jest wolny - na poziomie modelu
    # sprawdzić format maila - dokumentacja django czy walidacja na poziomie pola (modelu) jak nie to dodac w serializerze
    # sprawdzić czy mail jest w uzyciu (czy musi byc unialne w bazie danych)
    # mozna stworzyć usera z mailem lub bez

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        email = validated_data.get("email")

        try:
            validate_password(password)
        except ValidationError as e:
            raise exceptions.ValidationError(e)
        else:


