# Generated by Django 4.0.6 on 2022-07-24 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0022_alter_notification_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='update_time',
            field=models.TextField(default=datetime.datetime(2022, 7, 24, 22, 11, 34, 714564), verbose_name='update_time'),
        ),
    ]