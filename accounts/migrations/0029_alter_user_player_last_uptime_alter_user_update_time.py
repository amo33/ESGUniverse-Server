# Generated by Django 4.0.6 on 2022-07-23 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_user_player_last_uptime_alter_user_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='player_last_uptime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 16, 26, 13, 143171), verbose_name='recentaccess'),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 23, 16, 26, 13, 143288), verbose_name='recentupdate'),
        ),
    ]