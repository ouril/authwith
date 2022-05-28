from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from main.models import MyModel
from main.serializers import UserSerializer, MyModelSer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class MyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = MyModel.objects.all()
    serializer_class = MyModelSer


def somi(request, some):

    if some == 1:
        print("Это один вашу мать!!!")



    return JsonResponse({
        'foo':request.path,
        'dsd': request.method,
        'ds': some,
    })