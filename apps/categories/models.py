from django.db import models
from apps.core.models import Descriable, Timestampable


# Create your models here.

class Category(Descriable, Timestampable):
    CATE_TYPE = (
        (1, 'Post'),
        (2, 'Video'),
    )
    type = models.IntegerField(choices=CATE_TYPE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'
