from django.shortcuts import render, get_object_or_404
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination
from .paginators import ArticlePaginator

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePaginator

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# class ArticleList(APIView):
#     pagination_class = ArticlePaginator
    
#     def get(self, request, format=None):
#         queryset = Article.objects.all()
#         serializer = ArticleSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]

# class AllUsers(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class DisplayUsers(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
    
# class DisplayUsers(generics.ListAPIView):
#     permission_classes = [IsAdminUser]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class CreateUser(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class CreateUser(generics.CreateAPIView):
#     permission_classes = [AllowAny]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class ListCreateUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        #permission_classes = [IsAdminUser] if self.request.method == "GET" else [AllowAny]
        #return [permisson() for permisson in permission_classes]
        
        return [IsAdminUser() if self.request.method == "GET" else AllowAny()]


@api_view(["GET"])
def api_root(request, format=None):

    links = {
        "articles": reverse("articles", request=request, format=format),
        "users": reverse("users", request=request, format=format)
    }

    return Response(links)


