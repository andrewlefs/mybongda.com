# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20151115_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]
