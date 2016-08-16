# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0013_auto_20160222_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='image',
            field=models.ImageField(blank=True, max_length=500, upload_to='fixtures', default='fixture-default.jpg'),
        ),
    ]
