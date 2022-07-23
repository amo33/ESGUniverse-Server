# Generated by Django 4.0.6 on 2022-07-21 17:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0016_alter_user_player_last_uptime_alter_user_update_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('noti_type', models.IntegerField(default=0, verbose_name='noti_type')),
                ('title', models.TextField(blank=True, verbose_name='title')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('is_read', models.IntegerField(default=0, verbose_name='is_read')),
                ('update_time', models.DateTimeField(default=datetime.datetime(2022, 7, 22, 2, 14, 7, 178831), verbose_name='update_time')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]