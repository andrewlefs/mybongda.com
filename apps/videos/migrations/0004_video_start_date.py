# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20151116_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='start_date',
            field=models.DateField(auto_now=True, default=datetime.datetime(2015, 11, 22, 3, 55, 42, 719309, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
