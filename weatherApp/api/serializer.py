from .models import weatherData
from django.core.validators import MinValueValidator, MaxValueValidator
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
    lat = serializers.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    lon = serializers.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    detailType = serializers.ChoiceField( choices=TIME_CHOICES, default=ONE_HOUR)