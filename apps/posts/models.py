from django.db import models
from django.conf import settings
from apps.core.models import Descriable, Timestampable
from apps.categories.models import Category
from apps.tags.models import Tag
from django.core.urlresolvers import reverse_lazy


# Create your models here.

class Post(Descriable, Timestampable):
    image = models.ImageField(upload_to='posts', blank=True, max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category)
    url = models.URLField(blank=True, default='')
    image_source = models.URLField(blank=True, default='')

    # tags = models.ManyToManyField(Tag, db_table='post_tag',
    #                                         related_name='post')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('post:detail', kwargs={'pk': self.id, 'slug': self.slug})

    def get_image_url(self):
        if self.url:
            return self.image_source
        elif self.image:
            return self.image.url
        else:
            return settings.DEFAULT_IMAGE

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'
