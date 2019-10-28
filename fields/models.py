from django.core.validators import MinValueValidator, EmailValidator
from django.db import models
from django.utils import timezone

from sport.models import Sportsman
from user.models import User


class MyFields(models.Model):
    sportsman = models.ForeignKey(Sportsman, on_delete=models.CASCADE, blank=True)
    is_superfield = models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False)
    field_name = models.CharField(max_length=30)
    date_now = models.DateField(default=timezone.localdate)
    datetime = models.DateTimeField(default=timezone.now)
    field_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0, message="Price can't be less than 0")
        ]
    )
    email = models.EmailField()
    field_file = models.FileField(blank=True)
    field_image = models.ImageField(blank=True)
    field_year = models.IntegerField(validators=[MinValueValidator(0, message="Year can't be less than 0")])
    field_description = models.TextField()
    field_time = models.TimeField(blank=True)

    def __str__(self):
        return self.field_name
