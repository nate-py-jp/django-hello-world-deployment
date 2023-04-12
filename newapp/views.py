from django.shortcuts import render
from django.http import HttpResponse
from app1.settings import SECRET_KEY

def hello_world(request):
    return HttpResponse(f"Hello, world")
