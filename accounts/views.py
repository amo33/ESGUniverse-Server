from email import message
from socket import NI_NAMEREQD
from django.shortcuts import render, redirect

from .models import User, City, Map
from django.contrib import auth 
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .serializers import  BaseUserSerializer , UserinfoSerializer , CitySerializer
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import JsonResponse
cnt = 9
serializer_class = BaseUserSerializer

@csrf_exempt
def signup(request):
    try:
        data = json.loads(request.body)
        print(data)
        password = data['password']
        if password != None and data != None:
            username = data['name']
            email = data['email']
            nickname = data['nickname']
            try:
                user = User(name=username,password = password ,email = email,nickname=nickname, model = 0) 
                user.save()
                user_city = City(pid = user)
                user_city.save()
                user_map = Map(pid=user)
                user_map.save()
                # cnt+=1
                print(Map.objects.all())
            except IntegrityError:
                if User.objects.filter(email=email).exists():
                    print('Email already used!')
                elif User.objects.filter(nickname = nickname).exists(): # nickname도 integrity를 주었기 때문에 변경을 해야하는지 고민중
                    print("nickname already used!")
                
                return HttpResponse('SIGNUP_FAIL_EMAIL')
            
            return HttpResponse("SIGNUP_SUCCESS")
    except Exception as e:
        return HttpResponse("SIGNUP_FAIL_ETC")

serializer_class = BaseUserSerializer
@csrf_exempt
def login(request):
    
    email = request.GET.get('email', None)
    password = request.GET.get('password', None)
    
    user_exists = User.objects.filter(email=email, password=password).exists()
    if user_exists:
        # print("testing",User.objects.filter(username= name).values()[0]['model_3dnum'])
        print(User.objects.filter(email=email, password=password))
        id_num = User.objects.get(email=email, password=password).pid
        print("User is found!")
        return HttpResponse("LOGIN_SUCCESS/PID:{}".format(id_num))
        # 존재하지 않는다면
    else:
        if User.objects.filter(email=email).exists():
            if user_exists == False:
                return HttpResponse("LOGIN_FAIL")
            return HttpResponse("LOGIN_FAIL_ETC")
        else:
            return HttpResponse("LOGIN_FAIL_NO_EMAIL")
        

# @csrf_exempt
# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('/')
#     return render(request, 'accounts/login.html')

@csrf_exempt
def load_profile(request):
    data = json.loads(request.body)
    user_id = int(data['pid'])
    print(user_id)
    info = User.objects.filter(pid=user_id).values()
    
    if info != None:
        return HttpResponse(str(info).replace("<QuerySet [","").replace("]>","").replace("\'", "\""))
    else:
        return HttpResponse("NO_INFO")

@csrf_exempt 
def upload_profile(request):
    try:
        fetched_data = json.loads(request.body)
        print(fetched_data)
        email = fetched_data['email']
        password = fetched_data['password']
        my_id =User.objects.get(email=email, password=password).pid
        fetched_data.pop('email', None)
        fetched_data.pop('password', None)
        info =User.objects.filter(pid=my_id).update(**fetched_data)
    except IntegrityError:
        return HttpResponse("0")
    if info == None:
        return HttpResponse("0")
    return HttpResponse("1")

@csrf_exempt 
def withdraw_membership(request):
    try:
        user_id = json.loads(request.body)['pid']
        User.objects.filter(pid=user_id).delete()
    except  Exception as e:
        return HttpResponse("0")
    return HttpResponse("1")

@csrf_exempt 
def update_player_model(request):
    data = json.loads(request.body)
    try:
        user_id= int(data['pid'])
        model_num = data['model']
        User.objects.filter(pid=user_id).update(model=model_num)
    except Exception as e:
        return HttpResponse("0")
    return HttpResponse("1")

@csrf_exempt
def password_reset(request):
    data = json.loads(request.body)
    try:
        user_id= int(data['pid'])
        password = data['password']
        User.objects.filter(pid=user_id).update(password=password)
    except Exception as e:
        return HttpResponse("0")
    return HttpResponse("1")

# https://velog.io/@snowman39/Django-%EC%97%90%EC%84%9C-%EC%9D%B4%EB%A9%94%EC%9D%BC-%EB%B3%B4%EB%82%B4%EA%B8%B0-SMT-Gmail-API
@csrf_exempt
def email_temp_password(request):
    data = json.loads(request.body)
    try:
        user_id= int(data['pid'])
        password = 000000
        User.objects.filter(pid=user_id).update(password=password)

    except Exception as e:
        return HttpResponse("ETC_ERROR")
    email_address = User.objects.get(pid=user_id).email
    subject = "[Password Changed to"+ email_address + "]"
    to = [email_address]
    message = "비밀번호가 "+str(password)+ "로 바뀌었습니다. 다시 로그인하고 비밀번호 변경을 진행하시면 됩니다."
    EmailMessage(subject=subject,body=message, to=to)
    return HttpResponse("1")

@csrf_exempt
def list_up_city(request):
    try:
        data = json.loads(request.body)    
        count = int(data['count'])
        min_rank = int(data['minRanking'])
        max_rank = int(data['maxRanking'])
        print(min_rank, max_rank)
    except Exception as e:
        print("request data key error")
        return HttpResponse({["error"]})
    city_list = []
    if min_rank != 0:
        for i in range(count):
            #city_list.append("M"+str(min_rank+i).zfill(6)) # M000007 과 같은 형식을 추가 
            city_list.append(str(min_rank+i))
    elif max_rank != 0:
        for i in range(count):
            #city_list.append("M"+str(min_rank-i).zfill(6)) # M000007 과 같은 형식을 추가 
            city_list.append(str(max_rank-i))
    city_json = json.dumps(city_list) # 현재 Map의 키는 "M0006"와 같이 사용하지 않고, "6"으로 표현
    return HttpResponse(city_json)

@csrf_exempt
def load_city(request):
    try:
        data = int(json.loads(request.body)['pid'])
        print(data)

        info = City.objects.filter(pid_id=data).values()
        # print("1",info['fields'])
    except Exception as e:
        print("request data key error")
        return HttpResponse({"error"})

    return HttpResponse(info, content_type="application/json")

@csrf_exempt
def upload_city(request):
    try:
        data= json.loads(request.body)
        pid= int(data['pid'])
        user= User.objects.filter(pid=pid)
        # data['pid']=user 
        data.pop('pid', None)
        print(pid,data, user)
        City.objects.filter(pid=pid).update(**data)
        print(City.objects.filter(pid=user))
    except Exception as e:
        return HttpResponse("0")
    
    return HttpResponse("1")

@csrf_exempt
def update_donation(request):
    try:
        data = json.loads(request.body)    
        city_id = int(data['cid'])
        donation = int(data['donation_total'])
    except Exception as e:
        print("request data key error")
        return HttpResponse({"error"})
    try:
        City.objects.filter(cid=city_id).update(donation_total=donation)
    except Exception as e:
        return HttpResponse("0")
    print(City.objects.filter(cid=city_id).values())
    return HttpResponse("1")

@csrf_exempt
def load_map(request):
    try:
        data = json.loads(request.body)
        pid = int(data['pid'])
        # user = User.obects.get(pid=pid)
        info = Map.objects.filter(pid=pid).values()
        # map_json = json.dumps(info)
        # print(map_json)
    except Exception as e:
        return HttpResponse(e)

    return HttpResponse(info, content_type="application/json")


@csrf_exempt 
def upload_map(request):
    try:
        data = json.loads(request.body)
        pid = data['pid']
        data.pop('pid', None)
        Map.objects.filter(pid=pid).update(**data)
        
    except Exception as e:
        return HttpResponse(e)
    print(Map.objects.filter(pid=pid).values())
    return HttpResponse("1")