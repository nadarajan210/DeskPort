# Generated by Django 3.2.3 on 2021-06-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='field_length',
            field=models.IntegerField(default=0),
        ),
    ]