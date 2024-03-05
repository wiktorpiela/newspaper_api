from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('hello-world/', views.HelloWorldView.as_view(), name='hellowWorld'),
    path('article-list-create/', views.ArticleListCreate.as_view(), name='articleListCreate'),
    path('article-details/<int:pk>/', views.ArticleDetail.as_view(), name='articleDetail'),
    path('user-list-create/', views.UserView.as_view(), name='userListCreate'),
]
