from rest_framework import serializers
from streetsweeper.models import Street


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = (
            'id', 'neighborhood', 'name', 'street_type', 'even_week_day',
            'even_week_number', 'even_start_time', 'even_duration',
            'odd_week_day', 'odd_week_number', 'odd_start_time',
            'odd_duration', 'winter_hiatus')