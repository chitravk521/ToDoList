# Generated by Django 2.1.5 on 2019-02-26 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='updated',
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]