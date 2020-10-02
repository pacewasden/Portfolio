from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This is the Home Page\n"
                        "I am a senior at Weber State and work in IT right now\n")
