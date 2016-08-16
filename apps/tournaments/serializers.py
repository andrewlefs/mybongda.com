from rest_framework import serializers
from . import models


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tournament
        fields = ('id', 'name', 'slug')
