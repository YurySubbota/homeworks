from django.db import models


# Create your models here.

class Room(models.Model):
    picture = models.ImageField(null=True, blank=True, default=None, upload_to='media')
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Room'
        verbose_name = 'Room'


class Comment(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, null=False, blank=False, default='anonymous', unique=False)
    content = models.TextField(null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.nickname}, {self.created_at}'

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Comment'
        verbose_name = 'Comment'
