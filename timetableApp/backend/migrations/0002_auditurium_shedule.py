# Generated by Django 2.2.6 on 2019-12-20 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditurium',
            name='shedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Shedule', verbose_name='Расписание'),
        ),
    ]
