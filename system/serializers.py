# serializers.py
from rest_framework import serializers

from .models import TeamModel

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamModel
        fields = ('name', 'abbr')