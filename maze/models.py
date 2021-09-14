from django.db import models
from django.conf import settings


class Now(models.Model):
    u = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    now_floor = models.IntegerField(null=True)

    def __str__(self):
        return self.now_floor

    class Meta:
        db_table = 'now'
        verbose_name = '현재위치'
