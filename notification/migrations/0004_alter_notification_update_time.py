# Generated by Django 4.0.6 on 2022-07-21 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_alter_notification_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 2, 35, 52, 687922), verbose_name='update_time'),
        ),
    ]
