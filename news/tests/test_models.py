from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Article

#setup - uruchamia przed funkcjami obiekty i intancje potrzebne do testowania

class ArticleTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='122334')
        self.article = Article.objects.create(title='test title', text='test text', author=self.user)

    def test_article(self):
        article = Article.objects.get(id=self.article.id)
        self.assertEqual(article.title, self.article.title)
        self.assertEqual(article.text, self.article.text)
        self.assertEqual(article.author, self.article.author)