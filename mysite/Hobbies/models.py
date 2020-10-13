from django.db import models

# Create your models here.
class hobbies(models.Model):

    def __str__(self):
        return self.hobbies_name

#change hobbie_ photo to hobbies_photo
    hobbies_name=models.CharField(max_length=200)
    hobbies_type=models.CharField(max_length=200)
    hobbie_photo=models.CharField(max_length=500, default="https://i.ytimg.com/vi/Tz7EwqQFhjk/maxresdefault.jpg")