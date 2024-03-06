from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    pass_hash = models.CharField(max_length=255)
