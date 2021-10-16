from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    print("In Home views")
    return HttpResponse("Hello, this is Home view response...!")

def greet(request):
    print("In Greet views")
    return HttpResponse("Hello, this is Greet view response...!")

def function(request):
    print("In Function views")
    return HttpResponse("Hello, this is Function view response...!")