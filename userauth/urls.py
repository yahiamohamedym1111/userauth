"""userauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from iuser import views
from rest_framework import routers





#auth

r11 = routers.DefaultRouter()
r11.register('', views.checkUser)

r12 = routers.DefaultRouter()
r12.register('', views.checkCompany)

r7 = routers.DefaultRouter()
r7.register('', views.userRegister)

r8 = routers.DefaultRouter()
r8.register('', views.companyRegister)



urlpatterns = [
    path('admin/', admin.site.urls),


    #auth
    path('checkUser/', include(r11.urls)),
    path('checkCompany/', include(r12.urls)),
    path('userRegister/', include(r7.urls)),
    path('companyRegister/', include(r8.urls)),
]
