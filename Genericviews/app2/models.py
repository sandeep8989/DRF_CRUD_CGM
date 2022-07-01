from django.db import models

# Create your models here.

class Workermodel(models.Model):
    workerid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    