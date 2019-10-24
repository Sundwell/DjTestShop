from django import forms
from user.models import User
from django.utils import timezone


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = [
            'is_superuser',
            'is_active',
            'is_staff',
            'user_permissions',
            'groups',
        ]
