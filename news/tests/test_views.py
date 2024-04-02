from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Article
from django.urls import reverse
from rest_framework import status
from ..serializers import ArticleSerializer
import random

# data from Faker

class TestGetDeleteMethod(APITestCase):

    def setUp(self):
        self.random_idx = random.randint(0, 10)
        self.user = User.objects.create_user(username=f'testuser', password='122334')
        self.articles = [Article.objects.create(title=f'test_title_{i}', text=f'test_text_{i}', author=self.user) for i in range(11)]
        self.url_list = reverse('news:articleListCreate')
        self.url_retrieve = reverse('news:articleDetails', args = [self.random_idx])
        self.expected_data = ArticleSerializer(self.articles, many=True)

    def test_article_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_data.data)

    def test_article_retrieve(self):
        response = self.client.get(self.url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_data.data[self.random_idx-1])

    def test_article_delete(self):
        self.client.force_authenticate(self.user)
        response = self.client.delete(self.url_retrieve)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # put post / user
    
class TestPostMethod(APITestCase):

    def setUp(self):
        self.url_post = reverse('news:articleListCreate')
        self.user = User.objects.create_user(username=f'testuser', password='122334')
        self.client.force_authenticate(self.user)
        self.data = {
            'title': 'test title',
            'text': 'test text'
        }

    def test_create_article(self):
        response = self.client.post(self.url_post, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestPutMethod(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username=f'testuser', password='122334')
        self.client.force_authenticate(self.user)
        self.test_article = Article.objects.create(title='title', text='test text', author=self.user)
        self.url_put = reverse('news:articleDetails', args=[self.test_article.id])
        self.updated_article = {
            'title': 'new title',
            'text': 'test text'
        }

    def test_update_article(self):
        response = self.client.put(self.url_put, self.updated_article)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    




        
    

