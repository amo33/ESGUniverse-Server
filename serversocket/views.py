from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'serversocket/index.html')

def room(request, room_name):
    return render(request, 'serversocket/room.html', {
        'room_name': room_name
    })    