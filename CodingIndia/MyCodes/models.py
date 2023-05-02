from email.policy import default
from django.db import models
from datetime import date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=120)
    img = models.ImageField()
    
    def __str__(self):
        return self.name

# Create Playlist - Hackerrank Problem Solving
class Codings(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField(auto_now=True)
    content = RichTextField(blank=True)
    cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    proj = models.BooleanField(default=False)
    img = models.ImageField(blank=True, default="",null=True)
    author= models.CharField(max_length=150, default="Coding India")
    HTML = RichTextField(blank = True)
    Css = RichTextField(blank = True)
    Js = RichTextField(blank = True)

    def __str__(self):
        return self.name


# Created model for Python for beginners
# class PythonForBegginers(models.Model):
#     name = models.CharField(max_length=120)
#     date = models.DateField(auto_now=True)
#     content = RichTextField()
#     cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     proj = models.BooleanField(default=False)
#     author= models.CharField(max_length=150, default="Coding India")

#     def __str__(self):
#         return self.name

# class WebDesign(models.Model):
#     img = models.ImageField()
#     name = models.CharField(max_length=120)
#     date = models.DateField(auto_now=True)
#     cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     HTML = RichTextField(blank = True)
#     Css = RichTextField(blank = True)
#     Js = RichTextField(blank = True)
#     proj = models.BooleanField(default=False)
#     author= models.CharField(max_length=150, default="Coding India")

#     def __str__(self):
#         return self.name