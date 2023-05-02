from pyexpat import model
from django.db import models
from datetime import date
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
# from django.contrib.auth.models import User



# Create your models here.
class BlogsTags(TaggedItemBase):
    item = models.ForeignKey('AddBlog', on_delete=models.CASCADE)

    def __str__(self):
        return self.item

class Playlist(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(blank=True)
    img = models.ImageField()

    def __str__(self):
        return self.name

class SomeModel(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class AddBlog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.ImageField()
    pub_date = models.DateField(auto_now=True)
    category = models.CharField(max_length=200, blank=True)
    sub_category = models.CharField(max_length=200, blank=True)

    content = RichTextField()
    author= models.CharField(max_length=150, default="Codin India")
    readtime = models.IntegerField()
    tags = models.CharField(max_length=150)
    # dexc = models.TextField()
    play = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    somefield = models.ManyToManyField(SomeModel)

    def __str__(self):  
        return self.title


