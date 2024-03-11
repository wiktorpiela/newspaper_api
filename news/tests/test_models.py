from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Article

class ArticleTestCase(TestCase):

    def test_article(self):
        self.assertEqual(1, 1)
