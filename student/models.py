from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    year = models.IntegerField('year of studying')

    def __str__(self):
        return self.first_name + '' + self.last_name
