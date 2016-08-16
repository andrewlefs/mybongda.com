# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
