from django.db import models
from apps.core.models import Descriable, Timestampable

# Create your models here.

class Country(Descriable, Timestampable):
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'country'

    def __str__(self):
        return self.name

