from django.shortcuts import render

def index(request):

    return render(request,'chattest/index.html')



def room(request, room):
    return render(request, 'chattest/room.html', {"room": room})