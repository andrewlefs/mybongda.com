from django.db import models
from apps.core.models import Timestampable
from apps.fixtures.models import Fixture


# Create your models here.

class Match(Timestampable):
    fixture = models.OneToOneField(Fixture, related_name='match',
                                   primary_key=True)

    link_statistics = models.URLField(blank=True, default='')
    link_now_goal = models.URLField(blank=True, default='')
    link_betradar = models.URLField(blank=True, default='')
    link_odds = models.TextField(blank=True, default='')
    link_sopcast = models.URLField(blank=True, default='')

    frame_server_1 = models.TextField(blank=True, default='')
    frame_server_2 = models.TextField(blank=True, default='')
    frame_server_3 = models.TextField(blank=True, default='')
    frame_server_4 = models.TextField(blank=True, default='')
    frame_server_5 = models.TextField(blank=True, default='')
    frame_server_6 = models.TextField(blank=True, default='')
    frame_server_7 = models.TextField(blank=True, default='')
    frame_server_8 = models.TextField(blank=True, default='')

    frame_1xbet = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
        db_table = 'match'

    def __str__(self):
        return self.fixture.name
