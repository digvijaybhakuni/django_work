from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    createOn = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "<Employee id: {}, name: {}, email: {}>".format(self.id, self.name, self.email)


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/', max_length=254)
    emp = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return "<Profile id:{}, emp:{}>".format(self.id, self.emp)