from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

class ChatRoom(models.Model):
    total_members = models.IntegerField()
    members = models.ManyToManyField(Profile)


class Message(models.Model):
    text = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, default="")
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    