from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from sorl.thumbnail import get_thumbnail


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    createOn = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "<Employee id: {}, name: {}, email: {}>".format(self.id, self.name, self.email)


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/', max_length=254)
    thumb = ImageSpecField(source='image', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})
    emp = models.OneToOneField(Employee, on_delete=models.CASCADE)

    @property
    def thumbnail(self):
        if self.image:
            return get_thumbnail(self.image, '50x50', quality=90)
        return None

    def __str__(self):
        return "<Profile id:{}, emp:{}>".format(self.id, self.emp)


class BinaryStorage(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.FileField('data_file', null=False)
    data_binary = models.BinaryField('file_binary', null=True)
    name = models.CharField('file_name', max_length=100, null=False)

    def __str__(self):
        return "id: {}, name: {}".format(self.id, self.name)

