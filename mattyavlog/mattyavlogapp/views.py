from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, 'index.html')

def LenOfImage(request):
    len = 6
    data = {
        'len': str(len)
    }
    return JsonResponse(data)
