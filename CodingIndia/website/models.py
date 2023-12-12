from django.db import models
from datetime import date
from ckeditor.fields import RichTextField


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


class SkillsUsed(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=350)
    img = models.URLField()
    urllink = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    challenge = RichTextField()
    Solution = RichTextField()
    impact = RichTextField()
    conclusion = RichTextField()
    client = models.CharField(max_length=150)
    service = models.CharField(max_length=150)
    industry = models.CharField(max_length=150)

    desc = models.TextField()
    dateadded = models.DateField(auto_now_add=True)
    dateupdated = models.DateField(auto_now=True)
    skills = models.ManyToManyField(SkillsUsed)
    slug = models.SlugField()


    def __str__(self):
        return self.name