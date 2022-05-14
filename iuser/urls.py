from django.contrib import admin
from django.urls import path, include
from iuser import views
from rest_framework import routers



#auth
r11 = routers.DefaultRouter()
r11.register('', views.check)


r7 = routers.DefaultRouter()
r7.register('', views.userRegister)

r8 = routers.DefaultRouter()
r8.register('', views.companyRegister)



urlpatterns = [
    
    path('check/', include(r11.urls)),
    path('userRegister/', include(r7.urls)),
    path('companyRegister/', include(r8.urls)),

]