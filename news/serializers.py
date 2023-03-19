from rest_framework.serializers import ModelSerializer
from .models import Article

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "text", "date", "author",)
        read_only_fields = ("id", "date",) #te ktorych nie chce dostawac przy wysyłaniu requesta
