# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
        ('seasons', '0001_initial'),
        ('teams', '0001_initial'),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(default='', blank=True)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('type', models.IntegerField(default=1, choices=[(1, 'Main'), (2, 'Extra')])),
                ('country', models.ForeignKey(to='countries.Country')),
                ('season', models.ForeignKey(to='seasons.Season')),
                ('team_away', models.ForeignKey(to='teams.Team', related_name='fixture_away')),
                ('team_home', models.ForeignKey(to='teams.Team', related_name='fixture_home')),
                ('tournament', models.ForeignKey(to='tournaments.Tournament')),
            ],
            options={
                'verbose_name': 'Fixture',
                'verbose_name_plural': 'Fixtures',
                'db_table': 'fixture',
            },
        ),
    ]
