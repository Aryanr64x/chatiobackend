from django.urls import path
from .views import  index, room
urlpatterns = [
    path('/sockets/', index),
    path('/sockets/<str:room>/', room)
]
