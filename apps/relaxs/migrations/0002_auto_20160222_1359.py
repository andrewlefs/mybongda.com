# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('relaxs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relax',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=''),
        ),
    ]
