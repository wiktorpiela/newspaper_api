from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from news.models import Article
from news.serializers import ArticleSerializer


class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World!"})

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


