from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('articles-list-create/', views.ArticleListCreate.as_view(), name='articleListCreate'),
]
