from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("articles/", views.ArticleList.as_view()),
    path("articles/<int:pk>/", views.ArticleDetails.as_view()),
    path("users/", views.AllUsers.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)