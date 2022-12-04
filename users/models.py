from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    dp = models.ImageField(upload_to='images', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Test(models.Model):
    photo = models.ImageField(upload_to='images', null=True)