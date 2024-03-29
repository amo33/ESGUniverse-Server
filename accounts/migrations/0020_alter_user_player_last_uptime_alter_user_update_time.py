# Generated by Django 4.0.6 on 2022-07-21 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_user_player_last_uptime_alter_user_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='player_last_uptime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 2, 38, 46, 112356), verbose_name='recentaccess'),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 2, 38, 46, 112460), verbose_name='recentupdate'),
        ),
    ]
