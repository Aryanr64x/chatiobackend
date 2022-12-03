from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
import io
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def index(request):
    
    users = User.objects.all()
    users_data = UserSerializer(users, many = True)
    return HttpResponse(JSONRenderer().render(users_data.data))


@csrf_exempt
def createUser(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    userSerializer = UserSerializer(data = {"username": data['username'], "password": data["password"]})
    if(userSerializer.is_valid()):
        userSerializer.save()
        return HttpResponse(JSONRenderer().render(userSerializer.data))
    else:
        return HttpResponse("Cannot Create User!" )

    




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

    
        token['username'] = user.username
        

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
