from django.contrib import admin
from .models import Notification
# Register your models here.
class NotificationAdmin(admin.ModelAdmin):#admin 은 django 관리 페이지
    list_display = ('nid','pid')

admin.site.register(Notification)
