# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(default='', blank=True)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('season_start_date', models.DateField()),
                ('season_end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
                'db_table': 'season',
            },
        ),
    ]
