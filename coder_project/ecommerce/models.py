from django.db import models
from datetime import date


# Create your models here.

class Productos (models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    stock = models.BooleanField()
    price = models.IntegerField()
    date = models.DateField(default=date.today)



