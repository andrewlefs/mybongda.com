# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20151113_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='image',
            field=models.ImageField(default='', blank=True, max_length=500, upload_to='tournaments'),
        ),
    ]
