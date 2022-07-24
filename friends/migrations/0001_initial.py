# Generated by Django 4.0.6 on 2022-07-23 16:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0033_alter_user_player_last_uptime_alter_user_update_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.TextField(default=datetime.datetime(2022, 7, 24, 1, 10, 35, 87841), verbose_name='update_time')),
                ('pid1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_Friend_pid1', to='accounts.user')),
                ('pid2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_Friend_pid2', to='accounts.user')),
            ],
            options={
                'db_table': 'Friend_db',
            },
        ),
    ]