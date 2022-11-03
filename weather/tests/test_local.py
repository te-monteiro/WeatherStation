from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from weather.models import WeatherStation, Weather
from django.contrib.auth import get_user_model

class TestCreateWeatherStation(TestCase):
    def setUp(self):
        #self.user = User.objects.create(username='Teresa', password='test')
        self.user = get_user_model().objects.create_superuser(
                "admintest",
                "admintest@admintest.com",
                "admintest"
            )
        self.client = APIClient()
        self.client.login(username='admintest', password='admintest')
        self.user.save()
        WeatherStation.objects.create(name = 'GoeStation',  location = 'Goettingen', timestamp = '2012-05-20')

    def test_create_weather_station_instance(self):
        self.client.force_authenticate(self.user)
        weatherS = WeatherStation.objects.get(name="GoeStation")
        self.assertEqual(weatherS.location, 'Goettingen')

    def test_delete_weather_station_instance(self):
        self.client.force_authenticate(self.user)
        weatherStat = WeatherStation.objects.get(name="GoeStation")
        print(weatherStat.location, 'Goettingen')
        print(weatherStat.pk, 'pk')
        instance = WeatherStation.objects.get(id= 1)
        instance.delete()
        print(instance , "INSTANCE")
        print(weatherStat.location , "location")
#refresh db -- command


"""
class TestCreateWeather(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Teresa', password='test')
        self.client = APIClient()
        self.user.save()
        WeatherStation.objects.create(name = 'GoeStation',  location = 'Goettingen', timestamp = '2012-05-20')
        weatherSta = WeatherStation.objects.get(name="GoeStation")
        Weather.objects.create(weather_station = weatherSta.pk, temperature = '18', rainfall = '0.11', humidity = '0.88', air_pressure = '1.013', wind_speed = '3', timestamp = '2012-05-20')

    def test_create_weather_instance(self):
        self.client.force_authenticate(self.user)
        weatherSta = WeatherStation.objects.get(name="GoeStation")

        request = Weather.objects.get(name="GoeStation")
        #self.assertEqual(weatherSta.val, 1)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
"""

