# Generated by Django 4.0.6 on 2022-07-23 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0017_alter_notification_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='update_time',
            field=models.TextField(default=datetime.datetime(2022, 7, 24, 1, 10, 35, 85905), verbose_name='update_time'),
        ),
    ]
