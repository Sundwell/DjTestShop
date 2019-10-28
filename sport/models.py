from django.db import models


class Sportsman(models.Model):
    name = models.CharField(max_length=20)
    KINDS = [
        ('Street Workout', 'Street Workout'),
        ('Athletics', 'Athletics'),
        ('Power Lifting', 'Power Lifting'),
        ('ESports', 'ESports'),
    ]
    kind = models.CharField('Kind of sport', max_length=20, choices=KINDS)
    SIZES = [
        ('Big', 'Big'),
        ('Medium', 'Medium'),
        ('Small', 'Small'),
    ]
    gym_name = models.CharField(max_length=20)
    size = models.CharField(max_length=10, choices=SIZES)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    age = models.IntegerField()
    about = models.TextField()
    photo = models.ImageField(upload_to='sport/images/')

    def __str__(self):
        return self.name
