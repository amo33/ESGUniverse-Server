from . import views
from django.urls import path
urlpatterns = [
    
    path('accept_friend', views.accept_friend, name='accept_friend'),
    path('delete_friend', views.delete_friend, name='delete_friend'),
    path('load_friend_list',views.load_friend_list, name='load_friend_list')
    # path('upload_noti_detail', views.upload_noti_detail, name='upload_noti_detail'),
    # path('load_noti_detail', views.load_noti_detail, name='load_noti_detail'),
    # path('read_noti',views.read_noti, name = 'read_noti'),
  
]
