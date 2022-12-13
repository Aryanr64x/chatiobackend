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
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
from .models import Test
import base64
from django.core.files.base import ContentFile

from PIL import Image

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def index(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many = True)
    return HttpResponse(JSONRenderer().render(serializer.data))




@csrf_exempt
def createUser(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    userSerializer = UserSerializer(data = {"username": data['username'], "password": data["password"]})

    if(userSerializer.is_valid()):
        userSerializer.save()
        profile = Profile(dp=None, user_id=userSerializer.data["id"])
        profile.save()
        return HttpResponse(JSONRenderer().render(userSerializer.data))
    else:
        # TODO : RETURN RESPONSE WITH ERROR
        return HttpResponse("Cannot Create User!" )




@permission_classes([IsAuthenticated])
@api_view(['POST'])
def updateProfile(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    imageBASE64 = data['image']
    request.user.profile.dp = ContentFile(base64.b64decode(imageBASE64), 'chatio'+str(request.user.id)+'.jpg');
    request.user.profile.save()
    return HttpResponse(JSONRenderer().render(ProfileSerializer(request.user.profile).data))













class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        
        token['username'] = user.username
        token['dp'] = ProfileSerializer(user.profile).data["dp"]
        

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
