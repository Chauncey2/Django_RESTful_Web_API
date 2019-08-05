from django.shortcuts import render
from rest_framework.response import Response

from .models import Name
from rest_framework.views import  APIView
from rest_framework import viewsets
from .serializers import NameSerializers
import json


class Login(viewsets.ModelViewSet):

    queryset  = Name.objects.all()

    serializer_class  = NameSerializers

    # def get(self,request,format=None): # 继承APIView
    #
    #     users=Name.objects.all()
    #
    #     serializer=NameSerializers(users,many=True)
    #
    #     return Response(serializer.data)




