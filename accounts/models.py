from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, blank=True, null=True)
    self_introduction = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
