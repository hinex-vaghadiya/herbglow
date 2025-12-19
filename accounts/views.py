from django.shortcuts import render
from django.http import request,HttpResponse

from rest_framework import viewsets
from accounts.models import User
from accounts.serializers import UserSerializer
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


def home(request):
    return HttpResponse("<h1> Hello </h1>")


