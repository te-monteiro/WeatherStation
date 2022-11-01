from weather.models import Weather, WeatherStation
from rest_framework import serializers


class WeatherStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStation
        fields = ["id", "name", "location", "timestamp"]


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ["id", "weather_station", "temperature" , "rainfall", "humidity", "air_pressure", "wind_speed", "timestamp"]