from django.db import models

from article.models import Article


# Create your models here.
class Comment(models.Model):
    nickname = models.CharField(max_length=120)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

