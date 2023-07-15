from django.db import models

class weatherData(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    expTime= models.DateTimeField()
    data=models.CharField(max_length=255)



