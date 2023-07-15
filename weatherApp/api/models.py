from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class weatherData(models.Model):
    lat = models.FloatField(
        validators=[
            MinValueValidator(-90),  # Minimum value constraint
            MaxValueValidator(90)  # Maximum value constraint
        ]
    )
    lon = models.FloatField(
        validators=[
            MinValueValidator(-180),  # Minimum value constraint
            MaxValueValidator(180)  # Maximum value constraint
        ]
    )
    expTime= models.DateTimeField()
    data=models.CharField(max_length=255)



