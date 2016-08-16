# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0002_auto_20151113_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='link_blank',
            field=models.URLField(default='', blank=True),
        ),
    ]
