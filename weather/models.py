from django.db import models

class WeatherStation(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now=False, null=True, blank=True)

class Weather(models.Model):
    weather_station = models.ForeignKey(WeatherStation, on_delete=models.SET_NULL, null=True, blank=True)
    temperature = models.FloatField()
    rainfall = models.FloatField()
    humidity = models.FloatField()
    air_pressure = models.FloatField()
    wind_speed = models.FloatField()
    timestamp = models.DateField(auto_now=False, null=True, blank=True)

    class Meta:
        #combination of infex or create index of specific field
        indexes = [models.Index(fields=['timestamp'])]


class dataWeather(models.Model):
    day = models.DateField(("Tag"), auto_now=True)
    AVG_LWET200 = models.FloatField("AVG_LWET200")
    AVG_RH200 = models.FloatField("AVG_RH200")




