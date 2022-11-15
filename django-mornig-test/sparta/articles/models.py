from user.models import User
from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(blank = True, upload_to="%Y/%m")
    like = models.ManyToManyField(User, related_name = "article_like", blank = True)


    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'article_id' : self.pk})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    content = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)