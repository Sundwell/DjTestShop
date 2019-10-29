from django import forms
from .models import Sportsman


class SportsmanForm(forms.ModelForm):

    class Meta:
        model = Sportsman
        exclude = (
            'None',
        )
