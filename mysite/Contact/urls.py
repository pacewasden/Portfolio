from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info')
]
