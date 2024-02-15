from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('hello-world/', views.HelloWorldView.as_view(), name='hellowWorld'),
]
