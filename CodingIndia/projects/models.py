from django.db import models

class Playlist(models.Model):
    name = models.CharField(max_length=150)
    last_modified = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    content = models.TextField(blank=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)

    author = models.CharField(max_length=30, default="Coding India")
    category = models.CharField(max_length=150)
    play = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
