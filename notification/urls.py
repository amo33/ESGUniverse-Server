from . import views
from django.urls import path
urlpatterns = [
    path('delete_noti', views.delete_noti, name='delete_noti'),
    path('load_noti_list', views.load_noti_list, name='load_noti_list'),
    path('upload_noti_detail', views.upload_noti_detail, name='upload_noti_detail'),
    path('load_noti_detail', views.load_noti_detail, name='load_noti_detail'),
    path('read_noti',views.read_noti, name = 'read_noti'),
    path('request_friend', views.request_friend, name='request_friend'),
]
