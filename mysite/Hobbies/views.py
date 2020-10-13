from django.shortcuts import render
from django.http import HttpResponse
from .models import hobbies
from  django.template import loader
# Create your views here.

def index(request):
    hobbies_list = hobbies.objects.all()
    template= loader.get_template('hobbies/index.html')
    context={}
    return HttpResponse(template.render(context, request))
