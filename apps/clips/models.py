from django.db import models
from django.conf import settings
from apps.core.models import Descriable, Timestampable


# Create your models here.
class Clip(Descriable, Timestampable):
    image = models.CharField(max_length=500, default='')
    tournament = models.CharField(max_length=255, blank=True, default='')
    frame = models.TextField(blank=True, default='')
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image
        else:
            return settings.DEFAULT_IMAGE

    class Meta:
        verbose_name = 'Clip'
        verbose_name_plural = 'Clips'
        db_table = 'clip'
