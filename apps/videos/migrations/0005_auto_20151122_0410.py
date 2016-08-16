# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_video_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='start_date',
            new_name='match_date',
        ),
    ]
