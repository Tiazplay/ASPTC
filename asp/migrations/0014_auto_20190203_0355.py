# Generated by Django 2.1.5 on 2019-02-03 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asp', '0013_auto_20190127_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 3, 3, 55, 23, 356649)),
        ),
    ]