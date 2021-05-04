from django.http import HttpResponse
from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from ..models import BBCNews, NikkeiNews
from .serializer import BBCNewsSerializer, NikkeiNewsSerializer

# Create your views here.
class BBCNewsViewSet(viewsets.ModelViewSet):
    queryset = BBCNews.objects.all()
    serializer_class = BBCNewsSerializer




class NikkeiNewsViewSet(viewsets.ModelViewSet):
    queryset = NikkeiNews.objects.all()
    serializer_class = NikkeiNewsSerializer
