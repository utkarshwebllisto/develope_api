from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import path,include
from .import views
from my_api.views import  UserViewSet



urlpatterns=[
     path('', UserViewSet, name='UserViewSet'),
     path('UserViewSet/delete/<int:pk>/', UserViewSet, name='UserViewSet')
]