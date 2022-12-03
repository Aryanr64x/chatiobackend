from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 255)
    password = serializers.CharField(write_only = True)
    id = serializers.IntegerField(read_only = True)

    def create(self, validated_data):
        user = User(username=validated_data["username"],  password=make_password(password=validated_data["password"], hasher="bcrypt_sha256"))
        user.save()
        return user;


