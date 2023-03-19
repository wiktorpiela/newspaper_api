from django.urls import path
from . import views

urlpatterns = [
    path("articles/", views.article_list),
    path("articles/<int:articleID>/", views.article_details),
]