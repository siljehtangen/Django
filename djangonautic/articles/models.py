from turtle import title
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.Charfield(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)