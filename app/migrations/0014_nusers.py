# Generated by Django 3.2.3 on 2021-06-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_staffss'),
    ]

    operations = [
        migrations.CreateModel(
            name='nusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]