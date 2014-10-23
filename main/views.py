from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello this is main page+')

def contacts(request):
    return HttpResponse('hello this is contacts page')