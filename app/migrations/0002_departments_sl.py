# Generated by Django 3.2.3 on 2021-06-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='sl',
            field=models.IntegerField(default=0),
        ),
    ]
