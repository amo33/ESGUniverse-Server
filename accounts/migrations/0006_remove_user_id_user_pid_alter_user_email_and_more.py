# Generated by Django 4.0.6 on 2022-07-20 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_player_last_uptime_alter_user_update_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='pid',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='player_last_uptime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 20, 14, 54, 57, 361265), verbose_name='recentaccess'),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 20, 14, 54, 57, 361443), verbose_name='recentupdate'),
        ),
    ]