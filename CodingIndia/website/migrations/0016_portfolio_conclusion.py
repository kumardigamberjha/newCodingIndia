# Generated by Django 4.2.4 on 2023-12-12 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_portfolio_solution_alter_portfolio_challenge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='conclusion',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
