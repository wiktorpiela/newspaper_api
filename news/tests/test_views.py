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
        self.random_idx = random.randint(1, 10)
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

class TestUnauthRequests(APITestCase):

    def setUp(self):
        self.url_post = reverse('news:articleListCreate')
        self.url_put_delete = reverse('news:articleDetails', args = [1])
        self.url_put_delete_notfound = reverse('news:articleDetails', args = [2])
        self.user = User.objects.create_user(username=f'testuser', password='122334')
        self.test_article = Article.objects.create(title='title', text='test text', author=self.user)
        self.data = {
            'title': 'test title',
            'text': 'test text'
        }

    def test_article_unauth_post(self):
        response = self.client.post(self.url_post, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_article_unauth_delete(self):
        response = self.client.delete(self.url_put_delete)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_article_notfound_delete(self):
        response = self.client.delete(self.url_put_delete_notfound)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_article_notfound_update(self):
        response = self.client.put(self.url_put_delete_notfound, self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class TestIncompleteData(APITestCase):

    def setUp(self):
        self.url_post = reverse('news:articleListCreate')
        self.url_put = self.url_put_delete = reverse('news:articleDetails', args = [1])
        self.user = User.objects.create_user(username=f'testuser', password='122334')
        self.test_article = Article.objects.create(title='title', text='test text', author=self.user)
        self.client.force_authenticate(self.user)
        self.data_incompete = {
            'title': 'test title abc',
        }
        self.data_complete = {
            'title': 'test title',
            'text': 'test text'
        }

    def test_article_create_incomplete_data(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(self.url_post, self.data_incompete)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_article_update_incomplete_data(self):
        self.client.force_authenticate(self.user)
        response = self.client.put(self.url_put, self.data_incompete)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_permission(self):
        self.not_author = User.objects.create_user(username=f'not author', password='122334')
        self.client.force_authenticate(self.not_author)
        response = self.client.put(self.url_put, self.data_complete)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)





    




        
    

