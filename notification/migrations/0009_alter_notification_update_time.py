# Generated by Django 4.0.6 on 2022-07-21 17:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0008_alter_notification_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 17, 44, 53, 683934, tzinfo=utc), verbose_name='update_time'),
        ),
    ]
