from django.db import models
from datetime import date
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.crypto import get_random_string
import sys
# from django.contrib.auth.models import User



# Create your models here.
class BlogsTags(TaggedItemBase):
    item = models.ForeignKey('AddBlog', on_delete=models.CASCADE)

    def __str__(self):
        return self.item

class Playlist(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(blank=True)
    img = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name



class AddBlog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.URLField(blank=True, null=True)
    pub_date = models.DateField(auto_now=True)
    category = models.CharField(max_length=200, blank=True)
    sub_category = models.CharField(max_length=200, blank=True)

    content = RichTextField()
    author= models.CharField(max_length=150, default="Coding India")
    readtime = models.IntegerField()
    tags = models.CharField(max_length=150)
    play = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    slug = models.CharField(max_length=300)

    def __str__(self):  
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)

            random_string = get_random_string(length=6)

            self.slug = f'{base_slug}-{random_string}'

            counter = 1
            while AddBlog.objects.filter(slug=self.slug).exists():
                random_string = get_random_string(length=6)
                self.slug = f'{base_slug}-{random_string}'
                counter += 1

        super().save(*args, **kwargs)

