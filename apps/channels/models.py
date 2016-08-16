from django.db import models
from django.conf import settings
from apps.core.models import Timestampable, Descriable


# Create your models here.

class Channel(Descriable, Timestampable):
    SHOW_TYPE = (
        (1, 'Frame'),
        (2, 'Link'),
    )
    type = models.IntegerField(choices=SHOW_TYPE, default=1)
    image = models.ImageField(upload_to='channels', blank=True,
                              max_length=500, default='')
    link = models.URLField(blank=True, default='')
    frame = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'channel'

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return settings.DEFAULT_IMAGE
