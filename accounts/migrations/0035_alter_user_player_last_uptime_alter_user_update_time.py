# Generated by Django 4.0.6 on 2022-07-24 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_rename_main_misson_user_main_mission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='player_last_uptime',
            field=models.TextField(default=datetime.datetime(2022, 7, 24, 21, 37, 47, 691321), verbose_name='recentaccess'),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.TextField(default=datetime.datetime(2022, 7, 24, 21, 37, 47, 691434), verbose_name='recentupdate'),
        ),
    ]
