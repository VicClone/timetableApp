# Generated by Django 2.2.6 on 2019-12-05 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191205_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='staff',
        ),
    ]
