from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.





class Check(models.Model):
    userName = models.CharField(max_length=80, null = False, blank = False, unique = True)
    email = models.EmailField(max_length= 100, null = False, blank = False, unique = True)
    password = models.CharField(max_length=80, blank = False)
    is_user=models.BooleanField(default=True)

    def __str__(self):
        return self.userName



class UserRegister(models.Model):
    userName = models.CharField(max_length= 50 , null = False, blank = False, unique = True)
    email = models.EmailField(max_length= 100, null = False, blank = False, unique = True)
    phone =models.CharField(max_length = 15 , null = False, blank = False, unique = True)
    adress = models.CharField(max_length=200, null = False, blank = False)
    password = models.CharField(max_length=250,null = False, blank = False)

    def __str__(self):
        return self.userName


class CompanyRegister(models.Model):
    userName = models.CharField(max_length= 50, null = False, blank = False, unique = True )
    email = models.EmailField(max_length= 100, null = False, blank = False, unique = True)
    phone =models.CharField(max_length = 15, null = False, blank = False, unique = True)
    taxNumber = models.CharField(max_length=80, null = False, blank = False, unique = True)
    location = models.CharField(max_length=200, null = False, blank = False)
    password = models.CharField(max_length=150, null = False, blank = False)

    def __str__(self):
        return self.userName
