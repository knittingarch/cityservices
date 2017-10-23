# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiselectfield import MultiSelectField
from django.db import models


class Neighborhood(models.model):
    name = models.CharField(max_length=255)

class Street(models.model):

    WEEKDAY_CHOICES = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
        )
    WEEK_NUMBER = (
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
        )

    FOUR_HOURS = datetime.timedelta(hours=4) 
    SIX_HOURS = datetime.timedelta(hours=6)

    DURATIONS = (
        (FOUR_HOURS, '4 hours'),
        (SIX_HOURS, '6 hours'),
        )

    neighborhood = models.ForeignKey(
        'Neighborhood',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=255) 
    street_type = models.CharField(max_length=15)
    even_week_day = models.CharField(
        max_length=2,
        choices=WEEKDAY_CHOICES)
    even_week_number = MultiSelectField(choices=WEEK_NUMBER)
    even_start_time = models.DateTimeField()
    even_duration = models.DurationField(
        choices=DURATIONS,
        default=FOUR_HOURS)
    odd_week_day = models.CharField(
        max_length=2,
        choices=WEEKDAY_CHOICES)
    odd_week_number = MultiSelectField(choices=WEEK_NUMBER)
    odd_start_time = models.DateTimeField()
    odd_duration = models.DurationField(
        choices=DURATIONS,
        default=FOUR_HOURS)
    winter_hiatus = models.BooleanField(default=False)
