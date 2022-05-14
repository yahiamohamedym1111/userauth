from .models import CheckUser,CheckCompany,UserRegister,CompanyRegister
from rest_framework import serializers 
from django.contrib.auth.models import User



#auth


class  jsonCheckUser(serializers.ModelSerializer):
    class Meta:
        model = CheckUser
        fields = "__all__"

class  jsonCheckCompany(serializers.ModelSerializer):
    class Meta:
        model = CheckCompany
        fields = "__all__"


class  jsonUserRegister(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = "__all__"

class  jsonCompanyRegister(serializers.ModelSerializer):
    class Meta:
        model = CompanyRegister
        fields = "__all__"