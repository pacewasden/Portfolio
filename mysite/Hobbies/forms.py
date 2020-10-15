from django import forms
from .models import hobbies


class HobbieForm(forms.ModelForm):
     class Meta:
         model = hobbies
         fields=['hobbies_name','hobbies_type', 'hobbie_photo']

