from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from weather.models import WeatherStation, Weather

import pandas as pd
import csv, os

class TestCreateWeatherStation(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
                "admintest",
                "admintest@admintest.com",
                "admintest"
            )
        self.client = APIClient()
        self.client.login(username='admintest', password='admintest')
        self.user.save()
    
    #download file
    def download_weatherStation(self):
        self.client.force_authenticate(self.user)
        col_names = ["Tag" , "AVG_LWET200"]
        data_frame = pd.read_csv('./122_Alsheim_2018.csv', sep=";", decimal=",",na_values="-")
        return data_frame

    #we have ours weatherStation database
    def test_save_weatherstation_to_database(self):
        self.client.force_authenticate(self.user)
        data_frame = self.download_weatherStation()
        #data_frame.iterrows()
        for row in range(3):
            date = data_frame.loc[row , 'Tag'] + " " + data_frame.loc[row , 'Stunde']
            date_new = pd.to_datetime(date)
            WeatherStation.objects.create(name="station"+ str(row), timestamp=date_new, location=data_frame.loc[row ,  'AVG_LWET200'])
        
        weatherS = WeatherStation.objects.get(name="station"+ str(1))
        print("PRIMEIRO TESTE ", weatherS, weatherS.name, weatherS.timestamp, weatherS.location)

        all_weather_stations = WeatherStation.objects.all()
        for station in range(3):
            weatherS = WeatherStation.objects.get(name="station"+ str(station))
            print("WEATHER " , weatherS.name )
            path = os.path.join(weatherS, '/data/weather_stations/{weatherS.name}.csv')
            # path = "/weather/data/"
            print("PATH ", path)
            # #df.to_csv(path)
       
        #save_weatherstation_to_database(df, station.id)