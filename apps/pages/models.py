from django.db import models
from apps.core.models import Descriable, Timestampable


# Create your models here.

class Page(Descriable, Timestampable):
    content = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        db_table = 'page'
