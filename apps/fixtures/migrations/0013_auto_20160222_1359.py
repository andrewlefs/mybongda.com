# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fixtures', '0012_auto_20151215_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]
