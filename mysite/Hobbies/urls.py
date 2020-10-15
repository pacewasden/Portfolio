from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hobbies_id>', views.detail, name="detail"),
    path('add', views.create_hobbie, name='create_item'),
]