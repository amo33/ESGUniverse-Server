# Generated by Django 4.0.6 on 2022-07-23 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0015_alter_notification_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='update_time',
            field=models.TextField(default=datetime.datetime(2022, 7, 23, 23, 30, 48, 864624), verbose_name='update_time'),
        ),
    ]
