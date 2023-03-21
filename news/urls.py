from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path("articles/", views.article_list),
    path("articles/", views.ArticleList.as_view()),
    #path("articles/<int:articleID>/", views.article_details),
    path("articles/<int:pk>/", views.ArticleDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)