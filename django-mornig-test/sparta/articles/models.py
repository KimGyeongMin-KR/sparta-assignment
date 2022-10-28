from user.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()