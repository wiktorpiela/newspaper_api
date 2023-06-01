from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("articles/", views.ArticleList.as_view(), name="articles"),
    path("articles/<int:pk>/", views.ArticleDetails.as_view(), name="articleDetails"),
    path("users/", views.ListCreateUsers.as_view(), name="users"),
    path("", views.api_root, name="apiRoot"),
]

urlpatterns = format_suffix_patterns(urlpatterns)