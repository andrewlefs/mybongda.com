# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20151113_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(default='', upload_to='videos', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='score',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
    ]
