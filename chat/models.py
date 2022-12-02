from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    total_members = models.IntegerField()
    members = models.ManyToManyField(User)


class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    