# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0010_frameauto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frameauto',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
