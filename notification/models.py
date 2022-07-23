from datetime import datetime
from django.db import models
from django.utils import timezone
from accounts import models as production_models
# Create your models here.
class Notification(models.Model):
    nid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(production_models.User,on_delete=models.CASCADE)
    noti_type = models.IntegerField(verbose_name='noti_type',default=0)
    title = models.TextField(verbose_name='title',blank=True)
    content = models.TextField(verbose_name='content',blank=True)
    is_read = models.IntegerField(verbose_name='is_read',default = 0)
    update_time = models.TextField(verbose_name='update_time',default=datetime.now())
    def __str__(self):
        return str(self.nid) +'&' + str(self.pid)
    class Meta:
        db_table = 'Noti_db'