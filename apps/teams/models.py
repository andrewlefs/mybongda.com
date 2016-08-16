from django.db import models
from django.conf import settings
from apps.core.models import Descriable, Timestampable
from apps.countries.models import Country


# Create your models here.

class Team(Descriable, Timestampable):
    image = models.ImageField(upload_to='teams', blank=True,
                              max_length=500, default='')
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        db_table = 'team'

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return settings.DEFAULT_IMAGE
