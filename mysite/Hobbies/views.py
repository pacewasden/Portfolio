from django.shortcuts import render
from django.http import HttpResponse
from .models import hobbies
# Create your views here.

def index(request):
    hobbies_list = hobbies.objects.all()
    return HttpResponse(hobbies_list)
