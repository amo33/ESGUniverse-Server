from django.contrib import admin
from .models import User,City, Map
# Register your models here.
# class UserAdmin(admin.ModelAdmin):#admin 은 django 관리 페이지
#     list_display = ('username','password','email','model_3dnum')

admin.site.register(User)
admin.site.register(City)
admin.site.register(Map)