from rest_framework import serializers
from .models  import ChatRoom, Message
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from users.serializers import ProfileSerializer


class ChatRoomSerializer(serializers.ModelSerializer):
    members = ProfileSerializer(many=True)
    id = serializers.IntegerField()

    class Meta:
        model = ChatRoom
        fields = ['id' ,'members', 'total_members']

    
class MessageSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    # Its useless to send chatroom along with message . So just making it right only for making query 
    chatroom = ChatRoomSerializer(write_only = True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Message
        fields = ['id','text', 'profile', 'chatroom']

    def create(self, validated_data):

        print(validated_data["chatroom"])
        message = Message(text=validated_data["text"], profile_id=validated_data["profile"]["id"], chatroom_id=validated_data["chatroom"]["id"])
        message.save()
        return message



