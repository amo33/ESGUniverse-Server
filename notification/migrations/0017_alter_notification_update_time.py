# Generated by Django 4.0.6 on 2022-07-23 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0016_alter_notification_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='update_time',
            field=models.TextField(default=datetime.datetime(2022, 7, 24, 0, 54, 55, 583930), verbose_name='update_time'),
        ),
    ]
