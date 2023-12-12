# Generated by Django 4.2.4 on 2023-12-12 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_contactus_file_alter_contactus_lname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('img', models.URLField()),
                ('urllink', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('desc', models.TextField()),
                ('dateadded', models.DateField(auto_now_add=True)),
                ('dateupdated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='contactus',
            name='services',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
