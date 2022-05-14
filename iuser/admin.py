from django.contrib import admin
from .models import Check,UserRegister,CompanyRegister



# Register your models here.
admin.site.register(Check)
admin.site.register(UserRegister)
admin.site.register(CompanyRegister)