# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiselectfield import MultiSelectField
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight
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
    name = models.CharField(max_length=255)
    street_type = models.CharField(max_length=15, null=True, blank=True)
    even_week_day = models.CharField(
        max_length=2,
        choices=WEEKDAY_CHOICES)
    even_week_number = MultiSelectField(choices=WEEK_NUMBERS)
    even_start_time = models.TimeField()
    even_end_time = models.TimeField()
    odd_week_day = models.CharField(
        max_length=2,
        choices=WEEKDAY_CHOICES)
    odd_week_number = MultiSelectField(choices=WEEK_NUMBERS)
    odd_start_time = models.TimeField()
    odd_end_time = models.TimeField()
    winter_hiatus = models.BooleanField(default=False)

# def save(self, *args, **kwargs):
#     """
#     Use the pygments library to create a highlighted HTML
#     representation of the street entry.
#     """
#     lexer = get_lexer_by_name(self.language)
#     linenos = self.linenos and 'table' or False
#     options = self.title and {'title': self.title} or {}
#     formatter = HtmlFormatter(style=self.style, linenos=linenos,
#         full=True, **options)
#     self.highlighted = highlighted(self.code, lexer, formatter)
#     super(Street, self).save(*args, **kwargs)

