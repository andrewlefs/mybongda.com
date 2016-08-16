from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tag'
