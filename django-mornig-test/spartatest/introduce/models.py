from django.db import models

# Create your models here.
class AccessLog(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    location = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.location}에 {self.created_at}에 접속함'