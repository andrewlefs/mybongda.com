# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0007_auto_20151212_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='channels',
            field=models.ManyToManyField(db_table='fixture_channel', to='channels.Channel', related_name='fixtures'),
        ),
    ]
