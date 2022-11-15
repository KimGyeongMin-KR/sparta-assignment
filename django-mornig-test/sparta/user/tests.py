from urllib import response

from articles.models import Article, Comment
from user.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.

class TestView(APITestCase):

    def test_register(self):
        url = reverse('signup')
        data = {
            "email" : "test100@naver.com",
            "password" : "123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    # def test_login(self):
    #     url = reverse('token_obtain_pair')
    #     data = {
    #         "email" : "test100@naver.com",
    #         "password" : "123"
    #     }

class SetUpTestView(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.article_data = {
            "title" : "test",
            "content" : "test",
        }
        cls.data = {
            "email" : "test100@naver.com",
            "password" : "123"
        }
        cls.user = User.objects.create_user("test100@naver.com", "123")
        cls.article = Article.objects.create(author = cls.user, title = "test", content = "test")
        cls.comment = Comment.objects.create(author = cls.user, article_id = cls.article.id ,content = "test")


    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.data).data["access"]


class LoginTestView(APITestCase):

    def setUp(self):
        self.data = {
            "email" : "test100@naver.com",
            "password" : "123"
        }
        self.user = User.objects.create_user("test100@naver.com", "123")
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.data).data["access"]

    
    def test_tt(self):
        respone = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(respone.status_code, 200)


class GetUserTestView(LoginTestView):

    def test_ttt(self):
        print(self.access_token, 'sksksk')
        response = self.client.get(
            path = reverse('signup'),
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )

        self.assertEqual(response.data["email"], self.data["email"])