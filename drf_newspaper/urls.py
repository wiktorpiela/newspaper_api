from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include('news.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
