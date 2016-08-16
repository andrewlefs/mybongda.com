# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(default='', blank=True)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='tournaments', max_length=500)),
            ],
            options={
                'verbose_name': 'Tournament',
                'verbose_name_plural': 'Tournaments',
                'db_table': 'tournament',
            },
        ),
    ]
