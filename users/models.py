from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    dp = models.TextField(default = '')
    user = models.OneToOneField(User, on_delete=models.CASCADE)