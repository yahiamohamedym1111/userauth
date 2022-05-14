from django.contrib import admin
from .models import CheckUser,CheckCompany,UserRegister,CompanyRegister



# Register your models here.
admin.site.register(CheckUser)
admin.site.register(CheckCompany)
admin.site.register(UserRegister)
admin.site.register(CompanyRegister)