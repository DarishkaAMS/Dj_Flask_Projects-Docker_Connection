from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=240)
    image = models.CharField(max_length=240)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    user = User
