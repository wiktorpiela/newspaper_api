from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('article-list-create/', views.ArticleListCreate.as_view(), name='articleListCreate'),
    path('article-details/<int:pk>/', views.ArticleDetail.as_view(), name='articleDetails'),
    path('user-list-create/', views.UserView.as_view(), name='userListCreate'),
    path('user-details/<int:pk>/', views.UserDetail.as_view(), name='userDetails'),
    path('', views.APIRootView.as_view(), name='root'),
]
