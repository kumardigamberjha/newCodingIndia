# Generated by Django 4.2.4 on 2023-11-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_rename_name_contactus_fname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='lname',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
