from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=240)
    image = models.CharField(max_length=240)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"This is my name {self.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"My mane is {self.user.username}"
