from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
import io
from users.serializers import UserSerializer


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create(request):
    # Can be shopped to serializer?
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    user1 = User.objects.get(id=data['user_id'])
    chatroom = ChatRoom(total_members = 2)
    chatroom.save();
    chatroom.members.add(user1)
    chatroom.members.add(request.user)
    chatroom.save()  
    serializer = ChatRoomSerializer(chatroom)
    return HttpResponse(JSONRenderer().render(serializer.data))
    
    



@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def index(request):
    chatrooms = request.user.chatroom_set.all();
    chatroomsSerialized = ChatRoomSerializer(chatrooms, many = True)
    return HttpResponse(JSONRenderer().render(chatroomsSerialized.data))




#
@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def messageCreate(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    
    message = MessageSerializer(data = {
        "text": data['text'],
        "chatroom": data["chatroom"],
        "user": UserSerializer(request.user).data
    })
    if message.is_valid(raise_exception = True):
       message.save()
       return HttpResponse(JSONRenderer().render(message.data))
    else: 
       return HttpResponse(message.errors)




@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getMessages(request, id):
    chatroom = ChatRoom.objects.get(id = id)
    messages = chatroom.message_set.all()
    messagesSerializer = MessageSerializer(messages, many = True)
    print(messages)
    return HttpResponse(JSONRenderer().render(messagesSerializer.data))