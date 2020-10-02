from django.shortcuts import render
from django.http import HttpResponse
from .models import portfolio
# Create your views here.
def index(request):
    portfolio_list = portfolio.objects.all()
    return HttpResponse(portfolio_list)