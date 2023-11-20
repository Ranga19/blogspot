from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title