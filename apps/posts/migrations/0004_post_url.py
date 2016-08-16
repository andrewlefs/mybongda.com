# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
