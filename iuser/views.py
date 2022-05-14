from django.shortcuts import render
from rest_framework.response import Response
from .json import jsonCheck,jsonUserRegister,jsonCompanyRegister
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Check,UserRegister,CompanyRegister
from rest_framework import viewsets
# Create your views here.


#auth

class check(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = jsonCheck


class userRegister(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = jsonUserRegister

class companyRegister(viewsets.ModelViewSet):
    queryset = CompanyRegister.objects.all()
    serializer_class = jsonCompanyRegister