# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='tournament',
            field=models.CharField(default='', blank=True, max_length=255),
        ),
    ]
