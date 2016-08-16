from django.db import models
from django.conf import settings
from apps.core.models import Descriable, Timestampable
from apps.categories.models import Category


# Create your models here.

class Relax(Descriable, Timestampable):
    image = models.ImageField(upload_to='relaxs', max_length=255)
    frame = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return settings.DEFAULT_IMAGE

    class Meta:
        verbose_name = 'Relax'
        verbose_name_plural = 'Relaxs'
        db_table = 'relax'
