from django.db import models

# Create your models here.
class AccessLog(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    location = models.CharField(max_length=32)