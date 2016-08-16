from django.db import models
from apps.core.models import Descriable, Timestampable
from apps.seasons.models import Season
from apps.countries.models import Country
from apps.tournaments.models import Tournament
from apps.teams.models import Team
from apps.channels.models import Channel
from django.core.urlresolvers import reverse_lazy


# Create your models here.

class Fixture(Descriable, Timestampable):
    FIX_TYPE = (
        (1, 'Main'),
        (2, 'Extra'),
    )
    team_home = models.ForeignKey(Team, related_name='fixture_home')
    team_away = models.ForeignKey(Team, related_name='fixture_away')
    season = models.ForeignKey(Season)
    tournament = models.ForeignKey(Tournament)
    country = models.ForeignKey(Country)
    start_date = models.DateTimeField()
    type = models.IntegerField(choices=FIX_TYPE, default=1)
    link_blank = models.URLField(blank=True, default='')
    is_hot = models.BooleanField(blank=False, default=False)
    channels = models.ManyToManyField(Channel, db_table="fixture_channel", related_name='fixtures', blank=True)
    image = models.ImageField(upload_to='fixtures', blank=True,
                              max_length=500, default='fixture-default.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('fixture:detail', kwargs={'pk': self.id, 'slug': self.slug})

    class Meta:
        db_table = 'fixture'


class FrameAuto(Timestampable):
    url = models.CharField(max_length=255, unique=True)
    frame = models.TextField(blank=True, default='')

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'frame_auto'
