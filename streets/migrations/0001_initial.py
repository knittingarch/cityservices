# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-31 03:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood', models.CharField(choices=[('Winter Hill', 'Winter Hill'), ('East Somerville', 'East Somerville'), ('Prospect Hill', 'Prospect Hill'), ('Magoun Square', 'Magoun Square'), ('Ten Hills', 'Ten Hills'), ('Spring Hill', 'Spring Hill'), ('Powder House Square', 'Powder House Square'), ('Davis Square', 'Davis Square'), ('Ward Two', 'Ward Two'), ('Industrial Park', 'Industrial Park'), ('Mystic River', 'Mystic River'), ('West Somerville', 'West Somerville'), ('Tufts', 'Tufts')], max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('suffix', models.CharField(blank=True, choices=[('St', 'Street'), ('Ave', 'Avenue'), ('Ter', 'Terrace'), ('Hwy', 'Highway'), ('Rd', 'Road'), ('Ct', 'Court'), ('Cir', 'Circle'), ('Blvd', 'Boulevard'), ('Pk', 'Park'), ('Way', 'Way'), ('Pky', 'Parkway'), ('Dr', 'Drive')], max_length=15)),
                ('even_side_week_day', models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday')], max_length=2)),
                ('even_side_week_number', multiselectfield.db.fields.MultiSelectField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th')], max_length=7)),
                ('even_side_start_time', models.TimeField()),
                ('even_side_end_time', models.TimeField()),
                ('odd_side_week_day', models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('Th', 'Thursday'), ('F', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday')], max_length=2)),
                ('odd_side_week_number', multiselectfield.db.fields.MultiSelectField(choices=[('1', '1st'), ('2', '2nd'), ('3', '3rd'), ('4', '4th')], max_length=7)),
                ('odd_side_start_time', models.TimeField()),
                ('odd_side_end_time', models.TimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
