from django.shortcuts import render, redirect
from yaml import serialize
from .models import Notification
from django.contrib import auth 
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from accounts import models as production_models
import json
from django.template.loader import render_to_string
# Create your views here.

@csrf_exempt
def load_noti_list(request):
    try:
        data = json.loads(request.body)['pid']
    except Exception as e:
        print("Request body invalid structure")
        #return HttpResponse("0")
    
    info = Notification.objects.filter(pid=data).values('nid','noti_type','title','update_time','is_read')
    return HttpResponse(info)

@csrf_exempt
def upload_noti_detail(request):
    print(request.body)
    try:
        fetched_data = json.loads(request.body)
        print(fetched_data)
        pid = fetched_data['pid']
        user = production_models.User.objects.get(pid=pid)
        fetched_data['pid'] = user
        print(fetched_data)
    except Exception as e:
        print("json request loading error")
        return HttpResponse("0")
    note = Notification(**fetched_data)
    note.save() # 새로 업로드 후 저장 
    print(Notification.objects.all())
    return HttpResponse("1")

@csrf_exempt
def load_noti_detail(request):
    try:
        data = json.loads(request.body)['nid']
    except Exception as e:
        print("Request body invalid structure")
        #return HttpResponse("0")
    
    info = Notification.objects.filter(nid=data).values()
    return HttpResponse(info)

@csrf_exempt
def read_noti(request):
    try:
        data = json.loads(request.body)['nid']
    except Exception as e:
        print("No request input of nid")
        return HttpResponse("0")
    Notification.objects.filter(nid=data).update(is_read=1)
    print(Notification.objects.filter(nid=data).values())
    return HttpResponse("1")
@csrf_exempt
def delete_noti(request):
    try:
        data = json.loads(request.body)['nid']
    except Exception as e:
        print("Request body invalid structure")
        return HttpResponse("0")
    try:
        record = Notification.objects.get(nid=data)
        record.delete()
    except Exception as e:
        print("Delete Error")
        return HttpResponse("0")
    print(Notification.objects.all())
    return HttpResponse("1")