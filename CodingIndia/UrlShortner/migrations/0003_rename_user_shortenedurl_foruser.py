# Generated by Django 4.2.4 on 2023-12-28 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UrlShortner', '0002_shortenedurl_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortenedurl',
            old_name='user',
            new_name='foruser',
        ),
    ]
