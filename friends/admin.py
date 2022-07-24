from django.contrib import admin
from .models import Friend
# Register your models here.
# class FriendAdmin(admin.ModelAdmin):#admin 은 django 관리 페이지
#     list_display = ('pid1','pid2')

admin.site.register(Friend)