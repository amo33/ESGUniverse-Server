from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.

class User(models.Model):
    pid = models.AutoField(primary_key=True, verbose_name='pid')
    name = models.CharField(max_length=64, verbose_name='username') # verbose_name은 관리자에게 보이는 이름명이다.
    password = models.CharField(max_length=64, verbose_name='password')
    email = models.TextField(verbose_name = 'email', unique=True)
    nickname = models.CharField(max_length=32, verbose_name='nickname',unique=True)
    player_timezone = models.TextField('timezone',default='asia/seoul')
    model = models.IntegerField(verbose_name='model3D')
    player_last_uptime = models.TextField(verbose_name='recentaccess',default=datetime.now())
    main_mission = models.IntegerField(verbose_name='mainmission',default=0)
    sub_mission = models.TextField(verbose_name='submission',blank=True)
    last_pos = models.TextField(verbose_name='lastlocation',blank=True)
    last_city = models.TextField(verbose_name='lastcity',blank=True )
    balance = models.IntegerField(verbose_name='balance',default=0)
    badge_state = models.IntegerField(verbose_name='BadgeInfo',default=0)
    license_state = models.IntegerField(verbose_name='LicenseInfo',default=0)
    update_time = models.TextField(verbose_name='recentupdate',default=datetime.now())
    inventory= models.TextField(verbose_name='Inventory',blank=True)
    import_info = models.TextField(verbose_name='importinfo', blank=True)
    export_info = models.TextField(verbose_name='exportinfo',blank=True)
    energy_import = models.TextField(verbose_name='energyinfo',blank=True)
    vehicle_unlock = models.IntegerField(verbose_name='vechileInfo',default=0)
    fuel_info = models.TextField(verbose_name='fuelInfo',blank=True)
    def __str__(self):
        return str(self.pid)
    class Meta:
        db_table = 'user_db'

class City(models.Model):
    cid = models.AutoField(primary_key=True, verbose_name='cid')
    pid = models.ForeignKey(User,related_name="city", on_delete=models.CASCADE,verbose_name='person_id')
    population = models.IntegerField(verbose_name='population',default=0)
    happy_index = models.IntegerField(verbose_name='happy_index',default=0)
    eco_elec_energy_index = models.IntegerField(verbose_name='eco_elec_energy_index', default = 0)
    non_elec_energy_index = models.IntegerField(verbose_name='non_elec_energy_index', default=0)
    oil_energy_index = models.IntegerField(verbose_name='oil_energy_index',default=0)
    envi_score = models.IntegerField(verbose_name='envi_score',default=0)
    water_envi_score = models.IntegerField(verbose_name='water_envi_score',default=0)
    air_envi_score = models.IntegerField(verbose_name='air_envi_score',default=0)
    soil_envi_score = models.IntegerField(verbose_name='soil_envi_score',default=0)
    duty_tax_rate = models.IntegerField(verbose_name='duty_tax_rate',default=0)
    income_tax_rate = models.IntegerField(verbose_name='income_tax_rate',default=0)
    donation_total = models.IntegerField(verbose_name='donation_total',default=0)
    ranking = models.IntegerField(verbose_name='ranking', default = 6) # f 등급이 6으로 인덱스 찍혀서 6을 default로 진행했습니다.
    oil_traffic_score = models.IntegerField(verbose_name='oil_traffic_score',default=0)
    elec_traffic_score = models.IntegerField(verbose_name='elec_traffic_score',default=0)  
    subsidy_score = models.IntegerField(verbose_name='subsidy_score',default=0)
    import_total = models.IntegerField(verbose_name='import_total',default=0)
    export_total = models.IntegerField(verbose_name='export_total',default=0)

    def __str__(self):
        return str(self.cid) +'&' + str(self.pid)
    class Meta:
        db_table = 'city_db'

class Map(models.Model):
    mid = models.AutoField(primary_key=True, verbose_name='Mid')
    pid = models.ForeignKey(User,related_name="map", on_delete=models.CASCADE,verbose_name='person_id')  
    traffic_hub_unlock = models.IntegerField(verbose_name='traffic_hub_unlock',default=0)
    factory_level = models.IntegerField(verbose_name='factory_level',default = 0)
    factory_info = models.TextField(verbose_name='factory_info', blank=True)
    elec_factory_unlock = models.IntegerField(verbose_name='elec_factory_unlock',default = 0)
    elec_factory_info = models.TextField(verbose_name='elec_factory_info',blank=True)
    power_plant_unlock = models.IntegerField(verbose_name='power_plant_unlock',default=0)
    ess_info = models.IntegerField(verbose_name='ess_info',default=0)
    buttiport_unlock = models.IntegerField(verbose_name='buttiport_unlock',default=0)
    subsidy_info = models.TextField(verbose_name='subsidy_info')
    deco_item_position = models.TextField(verbose_name='deco_item_position',blank=True)
    sewerage_unlock = models.IntegerField(verbose_name='sewerage_unlock',default = 0)
    fiber_machine_unlock = models.IntegerField(verbose_name='fiber_machine_unlock',default=0)
    furnace_unlock = models.IntegerField(verbose_name='furnace_unlock',default=0)
    furnace_info = models.TextField(verbose_name='furnace_info',blank=True)

    def __str__(self):
        return str(self.mid) +'&' + str(self.pid)
    class Meta:
        db_table = 'map_db'
