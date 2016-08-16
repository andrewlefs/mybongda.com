# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20151113_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(default='', blank=True)),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(max_length=255, upload_to='relaxs')),
                ('frame', models.TextField(default='', blank=True)),
                ('category', models.ForeignKey(to='categories.Category')),
            ],
            options={
                'verbose_name': 'Relax',
                'verbose_name_plural': 'Relaxs',
                'db_table': 'relax',
            },
        ),
    ]
