from django.shortcuts import render
from rest_framework import viewsets
from .models import  *
from .serializers import *


# Create your views here.


class BaseProductView(viewsets.ModelViewSet):

    queryset = BaseProduct.objects.all()
    serializer_class = BaseProductSerializer

