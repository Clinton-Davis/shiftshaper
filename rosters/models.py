from django.conf import settings
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Shift(models.Model):
    day = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day}-{self.name}"


class Roster(models.Model):
    name = models.CharField(max_length=100, blank=True)
    week = models.PositiveSmallIntegerField(blank=False, null=False)
    # location =  Going to be a foreignkey
    start_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        # Calculate week number from start_date
        self.week = self.start_date.isocalendar()[1]
        super(Roster, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
