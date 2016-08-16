# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20151113_0617'),
        ('tournaments', '0005_remove_tournament_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='country',
            field=models.ForeignKey(to='countries.Country', default=189),
        ),
    ]
