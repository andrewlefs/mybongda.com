# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0003_fixture_link_blank'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='is_hot',
            field=models.BooleanField(default=False),
        ),
    ]
