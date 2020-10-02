from django.db import models

# Create your models here.
class hobbies(models.Model):

    def __str__(self):
        return self.hobbies_name


    hobbies_name=models.CharField(max_length=200)
    hobbies_type=models.CharField(max_length=200)