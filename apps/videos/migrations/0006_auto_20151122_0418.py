# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20151122_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='match_date',
            field=models.DateField(),
        ),
    ]
