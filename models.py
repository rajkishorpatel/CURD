from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    edesignation = models.CharField(max_length=30)
    esalery = models.IntegerField(max_length=30)
    eratings = models.FloatField()

