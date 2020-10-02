from django.db import models

# Create your models here.
class portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name


    portfolio_name=models.CharField(max_length=200)
    portfolio_type=models.CharField(max_length=200)