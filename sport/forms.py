from django import forms
from .models import Sportsman


class SportsmanForm(forms.ModelForm):

    class Meta:
        model = Sportsman
        fields = [
            'photo',
            'name',
            'age',
            'gym_name',
            'size',
            'cost',
            'kind',
            'about',
        ]
