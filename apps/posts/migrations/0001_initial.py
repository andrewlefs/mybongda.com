# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='posts', blank=True, max_length=255)),
                ('content', models.TextField()),
                ('category', models.ForeignKey(to='categories.Category')),
                ('tags', models.ManyToManyField(related_name='post', to='tags.Tag', db_table='post_tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'post',
            },
        ),
    ]
