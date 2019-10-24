from django import forms
from .models import Student


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']


class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = [
            '',
        ]