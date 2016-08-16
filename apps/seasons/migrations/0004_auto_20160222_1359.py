# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0003_auto_20151114_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]
