# Generated by Django 4.0.6 on 2022-07-24 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='update_time',
            field=models.TextField(default=datetime.datetime(2022, 7, 24, 16, 55, 5, 304138), verbose_name='update_time'),
        ),
    ]