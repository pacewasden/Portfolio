from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import hobbies
from .forms import HobbieForm
from django.template import loader


# Create your views here.

def index(request):
    hobbies_list = hobbies.objects.all()
    context = {'hobbies_list': hobbies_list, }
    return render(request, 'hobbies/index.html', context)


def detail(request, hobbies_id):
    stuff = hobbies.objects.get(pk=hobbies_id)
    context={
        'stuff':stuff
    }
    return render(request, 'hobbies/details.html', context)

def create