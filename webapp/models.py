from django.db import models
from datetime import datetime


# Create your models here.


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    createOn = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "email : " + self.email + ", name: " + self.name