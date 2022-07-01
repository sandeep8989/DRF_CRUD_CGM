
from django.db import models

# Create your models here.

class Empmodel(models.Model):
    empid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    Address = models.CharField(max_length=50)
