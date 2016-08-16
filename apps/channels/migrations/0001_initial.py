# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('type', models.IntegerField(choices=[(1, 'Frame'), (2, 'Link')], default=1)),
                ('image', models.ImageField(blank=True, default='', max_length=500, upload_to='channels')),
                ('link', models.URLField(blank=True, default='')),
                ('frame', models.TextField(blank=True, default='')),
            ],
            options={
                'db_table': 'channel',
            },
        ),
    ]
