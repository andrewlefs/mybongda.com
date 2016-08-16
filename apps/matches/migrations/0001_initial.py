# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0003_fixture_link_blank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('fixture', models.OneToOneField(primary_key=True, related_name='match', serialize=False, to='fixtures.Fixture')),
                ('link_statistics', models.URLField(default='', blank=True)),
                ('link_now_goal', models.URLField(default='', blank=True)),
                ('link_betradar', models.URLField(default='', blank=True)),
                ('link_odds', models.URLField(default='', blank=True)),
                ('link_sopcast', models.URLField(default='', blank=True)),
                ('frame_server_1', models.TextField(default='', blank=True)),
                ('frame_server_2', models.TextField(default='', blank=True)),
                ('frame_server_3', models.TextField(default='', blank=True)),
                ('frame_server_4', models.TextField(default='', blank=True)),
                ('frame_server_5', models.TextField(default='', blank=True)),
                ('frame_server_6', models.TextField(default='', blank=True)),
                ('frame_server_7', models.TextField(default='', blank=True)),
                ('frame_server_8', models.TextField(default='', blank=True)),
                ('frame_1xbet', models.TextField(default='', blank=True)),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
                'db_table': 'match',
            },
        ),
    ]
