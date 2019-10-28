from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    date_joined = models.DateField('date joined', auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    age = models.IntegerField(blank=True, default=0)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_permission(self):
        return self.is_superuser
    class Meta:
        unique_together = ['email', 'username']



