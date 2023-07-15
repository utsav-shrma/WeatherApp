from .models import weatherData
from rest_framework import serializers

class CoordinatePostSerializer(serializers.Serializer):
    ONE_HOUR = 'H'
    TWO_DAY = 'D'
    WEEK = 'W'
    TIME_CHOICES = [
        (ONE_HOUR, '1 One'),
        (TWO_DAY, '48 Hour'),
        (WEEK, '7 Days'),
    ]
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    detailType = serializers.ChoiceField( choices=TIME_CHOICES, default=ONE_HOUR)