from django.contrib.auth.models import User
from rest_framework import (
    fields,
    serializers,
)
from streets.models import (
    Street,
    NEIGHBORHOODS,
    WEEKDAY_CHOICES,
    WEEK_NUMBERS,
)


class UserSerializer(serializers.ModelSerializer):
    streets = serializers.PrimaryKeyRelatedField(many=True, queryset=Street.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'streets')


class StreetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    even_side_week_number = serializers.MultipleChoiceField(choices=WEEK_NUMBERS)
    odd_side_week_number = serializers.MultipleChoiceField(choices=WEEK_NUMBERS)

    class Meta:
        model = Street
        fields = (
            'id', 'owner', 'neighborhood', 'street_name', 'even_side_week_day',
            'even_side_week_number', 'even_side_start_time', 'even_side_end_time',
            'odd_side_week_day', 'odd_side_week_number', 'odd_side_start_time',
            'odd_side_end_time', 'winter_hiatus')
