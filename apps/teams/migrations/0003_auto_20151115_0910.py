# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20151113_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='', upload_to='teams', blank=True, max_length=500),
        ),
    ]
