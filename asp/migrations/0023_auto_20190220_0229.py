# Generated by Django 2.1.5 on 2019-02-19 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asp', '0022_auto_20190220_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compiler',
            name='compilationParams',
        ),
        migrations.AlterField(
            model_name='solution',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 2, 29, 54, 821283)),
        ),
    ]
