from django import forms
from django.core.exceptions import ValidationError

from baseball.models import Game


class PredictForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('t1_batAvg', 't2_batAvg', 't1_OBP', 't2_OBP', 't1_OPS', 't2_OPS', 't1_slug', 't2_slug', 't1_ERA', 't2_ERA')

    