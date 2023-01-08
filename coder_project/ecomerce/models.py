from django.db import models

# Create your models here.

class Productos (models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

class Carritos (models.Model):
    name = models.CharField(max_length=25)

class Cliente (models.Model):
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
