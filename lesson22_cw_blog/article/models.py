from django.db import models

from author.models import Author


# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=255,)
    article_content = models.TextField()
    article_date = models.DateTimeField()
    article_author = models.ManyToManyField(Author)
