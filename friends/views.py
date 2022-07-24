from django.shortcuts import render, redirect
from yaml import serialize
from .models import Friend
from django.contrib import auth 
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from accounts import models as production_models
import json
from django.db.models import Q
from django.template.loader import render_to_string
# Create your views here.

@csrf_exempt
def accept_friend(request):
    try:
        data = json.loads(request.body)
        pid1 = data['pid1']
        pid2 = data['pid2']
        user = production_models.User.objects.get(pid=pid1)
        user2 = production_models.User.objects.get(pid=pid2)
        data['pid1'] = user
        data['pid2'] = user2
    except Exception as e:
        print("Request body invalid structure")
        #return HttpResponse("0")
        
    info = Friend(**data)
    info.save()
    data['pid1'] , data['pid2'] = data['pid2'] , data['pid1']
    info2 = Friend(**data)
    info2.save()
    print(Friend.objects.all().values())
    return HttpResponse("2")

@csrf_exempt 
def delete_friend(request):
    try:
        data = json.loads(request.body)
        pid1 = data['pid1']
        pid2 = data['pid2']
        user = production_models.User.objects.get(pid=pid1)
        user2 = production_models.User.objects.get(pid=pid2)
        data['pid1'] = user
        data['pid2'] = user2
        Friend.objects.filter(Q(pid1=pid1, pid2= pid2)|Q(pid1=pid2, pid2=pid1)).delete() # 2개 삭제
        
    except Exception as e:
        print("Request body invalid structure")
        #return HttpResponse("0")
    
    
    print(Friend.objects.all().values())
    return HttpResponse("2")

@csrf_exempt
def load_friend_list(request):
    try:
        data = json.loads(request.body)
        pid = data['pid1']
        print("pid",pid)
        user_lst = Friend.objects.filter(pid1= pid).values_list('pid2',flat=True)
        print("user_lst",user_lst)
        nick_name_list = production_models.User.objects.filter(pid__in=user_lst).values_list('nickname')
    except Exception as e:
        return HttpResponse("0")
    nick_name_list = [val[0] for val in nick_name_list]
    print(nick_name_list)
    nickname_key = ["nickname"+str(i) for i in range(1,len(nick_name_list)+1)]
    nick_name_dictionary = dict(zip(nickname_key, nick_name_list))
    nick_name_return_dictionary = json.dumps(nick_name_dictionary)
    print(nick_name_return_dictionary)
    return HttpResponse(nick_name_return_dictionary)
    