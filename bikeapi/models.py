from django.db import models

class Bikes(models.Model):
     name=models.CharField(max_length=120)
     colour=models.CharField(max_length=120)
     cc=models.PositiveIntegerField()
     brand=models.CharField(max_length=120)
     price=models.PositiveIntegerField(null=True)
