from datetime import datetime
from django.db import models
from django.utils import timezone
from accounts import models as production_models
# Create your models here.
class Friend(models.Model):
    pid1 = models.ForeignKey(production_models.User,on_delete=models.CASCADE,related_name='friends_Friend_pid1')
    pid2 = models.ForeignKey(production_models.User,on_delete=models.CASCADE,related_name='friends_Friend_pid2')
    update_time = models.TextField(verbose_name='update_time',default=datetime.now())
    def __str__(self):
        return str(self.pid1) +'&' + str(self.pid2)
    class Meta:
        db_table = 'Friend_db'