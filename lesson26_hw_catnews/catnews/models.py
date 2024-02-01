from django.db import models


# Create your models here.

class News(models.Model):
    picture = models.ImageField(null=True, blank=True, default=None)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Comment(models.Model):
    nickname = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    news_id = models.ForeignKey('News', on_delete=models.CASCADE)
    comment_id = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.nickname} {self.pub_date}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'
