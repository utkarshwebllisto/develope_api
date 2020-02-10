from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from my_api.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer]) 
    
    # def delete(request,pk):
    # 	import pdb; pdb.set_trace()
    # 	queryset = User.objects.filter(id=pk) 
    # 	queryset.delete()
    

     # def update(self, request, *args, **kwargs):
     #    user = User.objects.filter()
     #    return Response(user)

