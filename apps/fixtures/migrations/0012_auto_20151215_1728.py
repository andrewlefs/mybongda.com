# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0011_auto_20151215_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frameauto',
            old_name='name',
            new_name='url',
        ),
    ]
