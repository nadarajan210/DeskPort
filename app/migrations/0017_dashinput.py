# Generated by Django 3.2.3 on 2021-06-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_password_nuserss_password1'),
    ]

    operations = [
        migrations.CreateModel(
            name='dashinput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dusers', models.IntegerField()),
                ('dstaffs', models.IntegerField()),
                ('ddepartments', models.IntegerField()),
                ('dknws', models.IntegerField()),
                ('dsatisfied', models.IntegerField()),
                ('dtickets', models.IntegerField()),
                ('dotickets', models.IntegerField()),
                ('dctickets', models.IntegerField()),
            ],
        ),
    ]
