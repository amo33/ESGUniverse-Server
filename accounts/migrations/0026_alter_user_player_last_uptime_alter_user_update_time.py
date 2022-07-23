# Generated by Django 4.0.6 on 2022-07-21 17:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_alter_user_player_last_uptime_alter_user_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='player_last_uptime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 17, 58, 43, 88420, tzinfo=utc), verbose_name='recentaccess'),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 17, 58, 43, 88552, tzinfo=utc), verbose_name='recentupdate'),
        ),
    ]
