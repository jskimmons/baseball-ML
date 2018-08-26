from .models import TodayGame
from rest_framework import serializers

class TodayGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodayGame
        fields = (
            't1_name',
            't2_name',
            't1_batAvg',
            't2_batAvg',
            't1_OBP',
            't2_OBP',
            't1_OPS',
            't2_OPS',
            't1_slug',
            't2_slug',
            't1_ERA',
            't2_ERA',
            'predictionTeam',
            'predictionInt',
            )