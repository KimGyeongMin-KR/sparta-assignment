from urllib import response
from articles.models import Article
from user.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.tests import SetUpTestView
from faker import Faker


from articles.serializers import ArticleSerializer, ArticleDetailSerializer


from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
from PIL import Image
import tempfile
# Create your tests here.

def get_temporary_image(temp_file):
    size = (200,200)
    color = (255,0,0,0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'png')
    return temp_file


class ArticleTestView(SetUpTestView):
    # def setUp(self):
        # super().setUp() # 리턴을 이것으로 해줭야하는 경우는? 지금 처럼하면 기존에 있던 것에 추가하는 격인가?
        

    def test_get_article_list(self):
        url = reverse("article_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_create_article(self):
        url = reverse("article_list")

        response = self.client.post(
            path = url,
            data = self.article_data,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            path = url,
            data = self.article_data,
        )
        self.assertEqual(response.status_code, 401)

        print(self.article_data)

    def test_create_article_with_img(self):

        temp_file = tempfile.NamedTemporaryFile()
        temp_file.name = "image.png"
        image_file = get_temporary_image(temp_file)
        image_file.seek(0)
        self.article_data["image"] = image_file

        response =self.client.post(
            path = reverse("article_list"),
            data = encode_multipart(data =self.article_data, boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, 201)


    def test_put_article(self):
        url = reverse('article_detail', args=[self.article.id,])

        response = self.client.put(
            path = url,
            data = {
                "title" : "ttitle",
                "content" : "ccontent"
            },
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_article(self):
        url = reverse('article_detail', args=[self.article.id,])

        response = self.client.delete(
            path = url,
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, 200)


class CommentTestView(SetUpTestView):

    def test_create_comment(self):
        url = reverse('article_commnet', kwargs={'article_id': self.article.id })
        response = self.client.post(
            path = url,
            data = {
                "content" : "kkk"
            },
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code, 201)

    def test_create_comment(self):
        url = reverse('article_detail', kwargs={'article_id': self.article.id, 'comment_id' : self.comment.id  })
        response = self.client.put(
            path = url,
            data = {
                "content" : "kkkkk"
            },
            HTTP_AUTHORIZATION = f"Bearer {self.access_token}"
        )
        print(response)
        self.assertEqual(response.status_code, 201)



class ArticleReadTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker()
        cls.articles = []
        for i in range(10):
            cls.user= User.objects.create_user(f"{cls.faker.name()}@naver.com", cls.faker.word())
            cls.articles.append(Article.objects.create(title=cls.faker.sentence(), content = cls.faker.sentence(), author = cls.user))

    def test_get_aricle(self):
        for article in self.articles:
            url = article.get_absolute_url()
            response = self.client.get(url)
            serializer = ArticleDetailSerializer(article).data
            for key, value in serializer.items():
                self.assertEqual(response.data[key], value)
