from django.db import models

from apps.core.models import Descriable, Timestampable

# Create your models here.

class Season(Descriable, Timestampable):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'
        db_table = 'season'
