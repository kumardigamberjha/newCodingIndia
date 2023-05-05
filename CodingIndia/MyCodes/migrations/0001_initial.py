# Generated by Django 4.0.1 on 2022-12-25 05:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Codings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('date', models.DateField(auto_now=True)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('proj', models.BooleanField(default=False)),
                ('img', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('author', models.CharField(default='Coding India', max_length=150)),
                ('HTML', ckeditor.fields.RichTextField(blank=True)),
                ('Css', ckeditor.fields.RichTextField(blank=True)),
                ('Js', ckeditor.fields.RichTextField(blank=True)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MyCodes.category')),
            ],
        ),
    ]