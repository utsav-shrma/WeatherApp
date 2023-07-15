from django.shortcuts import render
from .models import weatherData
from . import serializer
import requests
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, date, time, timedelta
from weatherApp import settings
import json
from django.http import JsonResponse

class ExternalAPIExampleView(APIView):
    
    def post(self,request):

        deserialized=serializer.CoordinatePostSerializer(data=request.data)
        deserialized.is_valid(raise_exception=True)
        data=deserialized.data

        current_time = timezone.make_aware(datetime.now(), timezone.get_default_timezone())
        forecast_string=settings.FORECAST_DATA_DEFAULT
        newExpTime = current_time+timedelta(minutes=settings.DEFAULT_EXP_TIME)

        detailType=data["detailType"]
        lat=data["lat"]
        lon=data["lon"]

        if(detailType=='H'):
            #forecast_string=settings.FORECAST_DATA_HOURLY
            newExpTime = current_time + timedelta(hours=1)
        if(detailType=='D'):
            #forecast_string=settings.FORECAST_DATA_DAILY
            newExpTime = current_time + timedelta(days=1)
        if(detailType=='W'):
            #forecast_string=settings.FORECAST_DATA_WEEKLY
            newExpTime = current_time + timedelta(days=7)

        requestWeatherData = weatherData.objects.filter(lat=lat , lon=lon).first()

        if(requestWeatherData is not None ):
            if(requestWeatherData.expTime>=current_time):
                return Response( json.loads(requestWeatherData.data),status=status.HTTP_200_OK)
            else:
                url = settings.URL.format(forecast_string,lat,lon,settings.ACCESS_TOKEN)
                response = requests.get(url)
                if (response.status_code == 200) :
                    requestWeatherData.expTime=newExpTime
                    requestWeatherData.data=json.dumps(response.json())
                    requestWeatherData.save()
                    return Response(response.json(),status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'API call failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            url = settings.URL.format(forecast_string,lat,lon,settings.ACCESS_TOKEN)
            response = requests.get(url)
            if response.status_code == 200 :
                new_object = weatherData(lat=lat, lon=lon,data=json.dumps(response.json()),expTime=newExpTime)
                new_object.save()
                return Response(response.json())
            else:
                return Response({'message': 'API call failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
