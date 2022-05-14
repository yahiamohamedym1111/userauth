from .models import Check,UserRegister,CompanyRegister
from rest_framework import serializers 
from django.contrib.auth.models import User



#auth


class  jsonCheck(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = "__all__"


class  jsonUserRegister(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = "__all__"

class  jsonCompanyRegister(serializers.ModelSerializer):
    class Meta:
        model = CompanyRegister
        fields = "__all__"