# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0006_auto_20151212_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='channels',
            field=models.ManyToManyField(to='channels.Channel', db_table='fixture_channel', related_name='fixture'),
        ),
    ]
