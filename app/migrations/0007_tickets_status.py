# Generated by Django 3.2.3 on 2021-06-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_tickets_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]