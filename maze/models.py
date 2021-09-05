from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    register_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = '유저'
        verbose_name_plural = '유저'


class Now(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    now_floor = models.CharField(max_length=100)

    def __str__(self):
        return self.now_floor

    class Meta:
        db_table = 'now'
        verbose_name = '현재위치'
