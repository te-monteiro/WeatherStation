from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from weather.models import WeatherStation, Weather

import pandas as pd
import csv


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

#    def download_weatherStation(self):
        
        #print("HEREeee ", data)

    def test_save_weatherstation_to_database(self):
        col_names = ["Tag" , "AVG_LWET200"]
        #df = pd.read_csv("./122_Alsheim_2018.csv",names=col_names, skiprows=[0]  )
        data_frame = pd.read_csv('./122_Alsheim_2018.csv', names=col_names, skiprows=[0], delimiter = ';')
        ola=data_frame.head()
        print(ola)

        for row in range(5):
            Weather.objects.create(name= row, timestamp=data_frame.columns["Tag"], location=data_frame.columns["AVG_LWET200"])
                
        print("DONE ")