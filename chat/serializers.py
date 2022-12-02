from rest_framework import serializers
from .models  import ChatRoom, Message
from users.serializers import UserSerializer
from django.contrib.auth.models import User



class ChatRoomSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    id = serializers.IntegerField()

    class Meta:
        model = ChatRoom
        fields = ['id' ,'members', 'total_members']

    
class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # Its useless to send chatroom along with message . So just making it right only for making query 
    chatroom = ChatRoomSerializer(write_only = True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Message
        fields = ['id','text', 'user', 'chatroom']

    def create(self, validated_data):

        print(validated_data["chatroom"])
        message = Message(text=validated_data["text"], user_id=validated_data["user"]["id"], chatroom_id=validated_data["chatroom"]["id"])
        message.save()
        return message



