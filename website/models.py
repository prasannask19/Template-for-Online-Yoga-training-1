from django.db import models

# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=30)
    phno = models.CharField(max_length=13)
    email = models.EmailField()
    dateofb=models.DateField()
    passwd = models.CharField(max_length=10)
    

class contact(models.Model):
    name = models.CharField(max_length=30)
    phno = models.CharField(max_length=13)
    email = models.EmailField()
    text=models.TextField()