# Generated by Django 4.0.6 on 2022-07-21 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_alter_notification_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 2, 40, 25, 908938), verbose_name='update_time'),
        ),
    ]