from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 퐈이팅 수~.")

# Create your views here.
