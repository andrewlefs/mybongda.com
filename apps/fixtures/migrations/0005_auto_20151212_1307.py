# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0001_initial'),
        ('fixtures', '0004_fixture_is_hot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fixture',
            options={},
        ),
        migrations.AddField(
            model_name='fixture',
            name='channels',
            field=models.ManyToManyField(related_name='fixture', to='channels.Channel'),
        ),
    ]
