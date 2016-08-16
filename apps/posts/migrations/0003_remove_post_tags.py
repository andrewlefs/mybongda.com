# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20151113_0617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
