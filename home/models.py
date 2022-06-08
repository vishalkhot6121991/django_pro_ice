import email
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=20)
    date=models.DateField()
    def __str__(self):
        return self.name
