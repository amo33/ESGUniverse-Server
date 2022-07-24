from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'serversocket/index.html')

def room(request, room_name):
    return render(request, 'serversocket/room.html', {
        'room_name': room_name
    })    

def serverStatus(request):
    try:
        data = request.headers 
    except Exception as e:
        return HttpResponse("0")
    
    return HttpResponse("hello")

def checkNowTime(request):
    try:
        data = request.headers 
    except Exception as e:
        return HttpResponse("0")
    
    return HttpResponse(datetime.now())