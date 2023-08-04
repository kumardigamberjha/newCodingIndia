from django.db import models

class Document(models.Model):
    pdf_file = models.FileField()
    word_file = models.FileField(blank=True, null=True, max_length=255)
