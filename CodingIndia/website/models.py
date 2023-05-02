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
