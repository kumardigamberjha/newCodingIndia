# Generated by Django 4.2.4 on 2023-11-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_addblog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='addblog',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='img',
            field=models.URLField(blank=True, null=True),
        ),
    ]
