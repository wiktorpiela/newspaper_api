from rest_framework import generics, permissions
from rest_framework.authtoken.admin import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
import random
from rest_framework import viewsets

from news.models import Article
from news.serializers import ArticleSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly, IsUserAccountOwner
from django.contrib.auth.models import User

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class APIRootView(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        pk = random.choice(articles).id
        links = {
            'articles': reverse('news:articleListCreate', request=request, format=format),
            'article-details': reverse('news:articleDetails', args = [pk], request=request, format=format),
            'users': reverse('news:userListCreate', request=request, format=format),
        }
        return Response(links)





