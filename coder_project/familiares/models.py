from django.db import models

# Create your models here.

class Familiares (models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    is_male = models.BooleanField()