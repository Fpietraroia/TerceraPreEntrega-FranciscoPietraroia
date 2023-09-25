from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=60)
    sname = models.CharField(max_length=60)
    mail = models.EmailField()

class Purchase(models.Model):

    obj = models.CharField(max_length=60)
    color = models.CharField(max_length=60)

class Location(models.Model):

    country = models.CharField(max_length=60)
    hood = models.CharField(max_length=60)
    num = models.IntegerField()
    d_date = models.DateField()