# Generated by Django 5.1.3 on 2024-11-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PolicyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='content',
            field=models.CharField(default=0, max_length=6000),
        ),
        migrations.AddField(
            model_name='policy',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]