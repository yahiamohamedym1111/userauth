from django.shortcuts import render
from rest_framework.response import Response
from .json import jsonCheckUser,jsonCheckCompany,jsonUserRegister,jsonCompanyRegister
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  CheckUser,CheckCompany,UserRegister,CompanyRegister
from rest_framework import viewsets
# Create your views here.


#auth

class checkUser(viewsets.ModelViewSet):
    queryset = CheckUser.objects.all()
    serializer_class = jsonCheckUser

class checkCompany(viewsets.ModelViewSet):
    queryset = CheckCompany.objects.all()
    serializer_class = jsonCheckCompany



class userRegister(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = jsonUserRegister

class companyRegister(viewsets.ModelViewSet):
    queryset = CompanyRegister.objects.all()
    serializer_class = jsonCompanyRegister