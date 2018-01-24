# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from multiselectfield import MultiSelectField

from django.db import models


NEIGHBORHOODS = (
    ('Winter Hill', 'Winter Hill'),
    ('East Somerville', 'East Somerville'),
    ('Prospect Hill', 'Prospect Hill'),
    ('Magoun Square', 'Magoun Square'),
    ('Ten Hills', 'Ten Hills'),
    ('Spring Hill', 'Spring Hill'),
    ('Powder House Square', 'Powder House Square'),
    ('Davis Square', 'Davis Square'),
    ('Ward Two', 'Ward Two'),
    ('Industrial Park', 'Industrial Park'),
    ('Mystic River', 'Mystic River'),
    ('West Somerville', 'West Somerville'),
    ('Tufts', 'Tufts'),
)

SUFFICES = (
    ('St', 'Street'),
    ('Ave', 'Avenue'),
    ('Ter', 'Terrace'),
    ('Hwy', 'Highway'),
    ('Rd', 'Road'),
    ('Ct', 'Court'),
    ('Cir', 'Circle'),
    ('Blvd', 'Boulevard'),
    ('Pk', 'Park'),
    ('Way', 'Way'),
    ('Pky', 'Parkway'),
    ('Dr', 'Drive'),
    )

WEEKDAY_CHOICES = (
    ('M', 'Monday'),
    ('T', 'Tuesday'),
    ('W', 'Wednesday'),
    ('Th', 'Thursday'),
    ('F', 'Friday'),
    ('Sa', 'Saturday'),
    ('Su', 'Sunday'),
)
WEEK_NUMBERS = (
    ('1', '1st'),
    ('2', '2nd'),
    ('3', '3rd'),
    ('4', '4th'),
)


class Street(models.Model):
    owner = models.ForeignKey('auth.User', related_name='streets', on_delete=models.CASCADE)
    neighborhood = models.CharField(
        max_length=255,
        choices=NEIGHBORHOODS)
    street_name = models.CharField(max_length=255)
    suffix = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        choices=SUFFICES)
    even_side_week_day = models.CharField(
        max_length=2,
        choices=WEEKDAY_CHOICES)
    even_side_week_number = MultiSelectField(choices=WEEK_NUMBERS)
    even_side_start_time = models.TimeField()
    even_side_end_time = models.TimeField()
    odd_side_week_day = models.CharField(
        max_length=2,
        choices=WEEKDAY_CHOICES)
    odd_side_week_number = MultiSelectField(choices=WEEK_NUMBERS)
    odd_side_start_time = models.TimeField()
    odd_side_end_time = models.TimeField()

    def winter_hiatus(self):
        hiatus_months = [1, 2, 3]
        today = datetime.date.today()
        current_month = today.month
        if current_month in hiatus_months:
            return True
        return False

