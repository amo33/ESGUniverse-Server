from rest_framework import serializers 
from .models import User , City , Map
class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['username','password','nickname','email','model_3dnum']

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'