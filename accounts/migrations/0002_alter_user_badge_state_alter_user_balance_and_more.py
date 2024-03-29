# Generated by Django 4.0.6 on 2022-07-17 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='badge_state',
            field=models.IntegerField(default=0, verbose_name='BadgeInfo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='balance'),
        ),
        migrations.AlterField(
            model_name='user',
            name='energy_import',
            field=models.TextField(blank=True, verbose_name='energyinfo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='export_info',
            field=models.TextField(blank=True, verbose_name='exportinfo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fuel_info',
            field=models.TextField(blank=True, verbose_name='fuelInfo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='import_info',
            field=models.TextField(blank=True, verbose_name='importinfo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='inventory',
            field=models.TextField(blank=True, verbose_name='Inventory'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_city',
            field=models.TextField(blank=True, verbose_name='lastcity'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_pos',
            field=models.TextField(blank=True, verbose_name='lastlocation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='license_state',
            field=models.IntegerField(default=0, verbose_name='LicenseInfo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='main_mission',
            field=models.IntegerField(default=0, verbose_name='mainmission'),
        ),
        migrations.AlterField(
            model_name='user',
            name='player_last_uptime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 17, 21, 15, 51, 323881), verbose_name='recentaccess'),
        ),
        migrations.AlterField(
            model_name='user',
            name='player_timezone',
            field=models.TextField(default='asia/seoul', verbose_name='timezone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sub_mission',
            field=models.TextField(blank=True, verbose_name='submission'),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 17, 21, 15, 51, 324074), verbose_name='recentupdate'),
        ),
        migrations.AlterField(
            model_name='user',
            name='vechile_unlock',
            field=models.IntegerField(default=0, verbose_name='vechileInfo'),
        ),
    ]
