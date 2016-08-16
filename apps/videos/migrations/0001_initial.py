# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('teams', '0001_initial'),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='videos', max_length=255)),
                ('frame', models.TextField(blank=True, default='')),
                ('score', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='categories.Category')),
                ('team_away', models.ForeignKey(related_name='video_away', to='teams.Team')),
                ('team_home', models.ForeignKey(related_name='video_home', to='teams.Team')),
                ('tournament', models.ForeignKey(to='tournaments.Tournament')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'db_table': 'video',
            },
        ),
    ]
