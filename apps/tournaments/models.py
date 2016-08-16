from django.db import models
from django.conf import settings
from apps.core.models import Descriable, Timestampable
from apps.countries.models import Country


# Create your models here.

class Tournament(Descriable, Timestampable):
    image = models.ImageField(upload_to='tournaments', blank=True,
                              max_length=500, default='')
    country = models.ForeignKey(Country, default=189)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'
        db_table = 'tournament'

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return settings.DEFAULT_IMAGE
