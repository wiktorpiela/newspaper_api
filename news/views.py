from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from news.models import Article
from news.serializers import ArticleSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly, IsUserAccountOwner
from django.contrib.auth.models import User

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello World!"})

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return [permissions.AllowAny() if self.request.method=='POST' else permissions.IsAdminUser()]

class UserDetail(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserAccountOwner]
