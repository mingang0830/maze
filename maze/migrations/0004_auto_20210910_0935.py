# Generated by Django 3.2.7 on 2021-09-10 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maze', '0003_auto_20210910_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='now_floor_id',
        ),
        migrations.AddField(
            model_name='now',
            name='u_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maze.user'),
        ),
        migrations.AlterField(
            model_name='now',
            name='now_floor',
            field=models.IntegerField(null=True),
        ),
    ]