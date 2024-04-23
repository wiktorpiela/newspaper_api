from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user-viewset', views.UserViewSet)

app_name = 'news'
urlpatterns = [
    path('article-list-create/', views.ArticleListCreate.as_view(), name='articleListCreate'),
    path('article-details/<int:pk>/', views.ArticleDetail.as_view(), name='articleDetails'),
    path('user-list-create/', views.UserView.as_view(), name='userListCreate'),
    path('user-details/<int:pk>/', views.UserDetail.as_view(), name='userDetails'),
    
    #path('', views.APIRootView.as_view(), name='root'),
    path('', include(router.urls)),
]
