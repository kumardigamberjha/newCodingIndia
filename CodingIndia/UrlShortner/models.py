from django.db import models



# Create your models here.
class ShortenedURL(models.Model):
    long_url = models.URLField()
    short_key = models.CharField(max_length=20, unique=True)
    on_date = models.DateTimeField(auto_now_add = True)
    foruser = models.CharField(max_length=150)

    class Meta:
        unique_together = (('long_url', 'foruser'))

    def __str__(self):
        return str(self.on_date)