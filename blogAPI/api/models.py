from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)