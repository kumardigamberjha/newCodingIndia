# Generated by Django 4.2.4 on 2023-11-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codings',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
    ]
