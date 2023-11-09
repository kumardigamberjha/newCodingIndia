from django.db import models
from datetime import date


class Quotes(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)

    def  __str__(self):
        return self.title

class Team(models.Model):
    name= models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    img = models.ImageField()

    def  __str__(self):
        return self.name


class ServicesModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class ContactUs(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=45)
    file = models.ImageField(null=True, blank=True)
    services = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name