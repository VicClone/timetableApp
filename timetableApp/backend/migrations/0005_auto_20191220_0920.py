# Generated by Django 2.2.6 on 2019-12-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20191220_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='day_week',
            field=models.CharField(default='пн', max_length=4, verbose_name='День недели'),
        ),
    ]