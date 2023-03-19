from django.shortcuts import render, get_object_or_404
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#widoki funkcyjne ----
@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True) #jesli przekazujemy queryset
        return JsonResponse(serializer.data, safe=False) #safe zeby przekazać dane w słowniku JsonResponse({"article":serializer.data})
    else:    # elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","DELETE","PUT"])
def article_details(request, articleID):
    my_article = get_object_or_404(Article,pk=articleID)
    # try:
    #     article = Article.objects.get(pk=articleId)
    # except Article.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer = ArticleSerializer(my_article)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "PUT":
        serializer = ArticleSerializer(instance = my_article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) #nie zawsze przekazywac status gdy put
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: #request.method=="DELETE":
        my_article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class based views ---


        
