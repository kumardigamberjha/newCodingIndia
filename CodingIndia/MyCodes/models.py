from email.policy import default
from django.db import models
from datetime import date
from ckeditor.fields import RichTextField

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Category(models.Model):
    name = models.CharField(max_length=120)
    img = models.ImageField()
    
    def save(self, *args, **kwargs):
        if self.img and not self.id:
            self.img = self.compressImage(self.img)
        super(Category, self).save(*args, **kwargs)

    def compressImage(self, uploadedImage):
        imageTemporary = Image.open(uploadedImage)

        # Convert the image to RGB mode to remove the alpha channel
        imageTemporary = imageTemporary.convert("RGB")

        outputIoStream = BytesIO()
        imageTemporaryResized = imageTemporary.resize((250, 150))
        imageTemporary.save(outputIoStream, format='WEBP', quality=85)  # Convert to WebP
        outputIoStream.seek(0)

        return InMemoryUploadedFile(
            outputIoStream,
            'ImageField',
            "%s.webp" % self.img.name.split('.')[0],
            'image/webp',  # Set the content type to 'image/webp'
            sys.getsizeof(outputIoStream),
            None
        )
    
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
    
    def save(self, *args, **kwargs):
        if self.img and not self.id:
            self.img = self.compressImage(self.img)
        super(Category, self).save(*args, **kwargs)

    def compressImage(self, uploadedImage):
        imageTemporary = Image.open(uploadedImage)

        # Convert the image to RGB mode to remove the alpha channel
        imageTemporary = imageTemporary.convert("RGB")

        outputIoStream = BytesIO()
        imageTemporaryResized = imageTemporary.resize((250, 150))
        imageTemporary.save(outputIoStream, format='WEBP', quality=85)  # Convert to WebP
        outputIoStream.seek(0)

        return InMemoryUploadedFile(
            outputIoStream,
            'ImageField',
            "%s.webp" % self.img.name.split('.')[0],
            'image/webp',  # Set the content type to 'image/webp'
            sys.getsizeof(outputIoStream),
            None
        )


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