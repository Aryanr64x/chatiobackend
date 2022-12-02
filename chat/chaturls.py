from django.urls import path
from .views import create, index, messageCreate, getMessages
urlpatterns = [
    path('/create/', create),
    path('/message/create/', messageCreate),
    path('/message/<int:id>', getMessages),
    path('/', index),
    

]