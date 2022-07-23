from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):#admin 은 django 관리 페이지
    list_display = ('username','password','email','model_3dnum')

admin.site.register(User)