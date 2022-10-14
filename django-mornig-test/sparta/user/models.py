from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'user'

    address = models.TextField(max_length = 500, blank = True)
    phone = models.CharField(max_length = 15)