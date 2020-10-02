from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This is the Contact Page: If you need to reach me please email "
                        "pacewasden@gmail.com")
def info(request):
    return HttpResponse("This is my information")