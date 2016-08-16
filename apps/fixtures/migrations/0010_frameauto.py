# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0009_auto_20151213_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrameAuto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('frame', models.TextField(blank=True, default='')),
            ],
            options={
                'db_table': 'frame_auto',
            },
        ),
    ]
