from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('serverStatus', views.serverStatus, name='serverStatus'),
    path('checkNowTime',views.checkNowTime, name='checkNowTime')
]