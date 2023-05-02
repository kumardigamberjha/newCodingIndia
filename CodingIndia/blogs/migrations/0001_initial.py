# Generated by Django 4.0.1 on 2022-12-25 05:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBlog',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='')),
                ('pub_date', models.DateField(auto_now=True)),
                ('category', models.CharField(blank=True, max_length=200)),
                ('sub_category', models.CharField(blank=True, max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('author', models.CharField(default='Codin India', max_length=150)),
                ('readtime', models.IntegerField()),
                ('dexc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('desc', models.TextField(blank=True)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='BlogsTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.addblog')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='addblog',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.playlist'),
        ),
        migrations.AddField(
            model_name='addblog',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
