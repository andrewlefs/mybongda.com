# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_source',
            field=models.URLField(blank=True, default=''),
        ),
    ]
