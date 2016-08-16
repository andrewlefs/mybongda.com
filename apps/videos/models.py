from django.db import models
from django.conf import settings
from apps.core.models import Descriable, Timestampable
from apps.categories.models import Category
from apps.teams.models import Team
from apps.tournaments.models import Tournament


# Create your models here.
class Video(Descriable, Timestampable):
    image = models.ImageField(upload_to='videos', max_length=255,
                              blank=True, default='')
    frame = models.TextField(blank=True, default='')
    score = models.CharField(max_length=255, blank=True, default='')
    team_home = models.ForeignKey(Team, related_name='video_home')
    team_away = models.ForeignKey(Team, related_name='video_away')
    category = models.ForeignKey(Category)
    tournament = models.ForeignKey(Tournament)
    match_date = models.DateField()

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return settings.DEFAULT_IMAGE

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        db_table = 'video'
