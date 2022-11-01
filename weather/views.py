from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action

from weather.models import WeatherStation, Weather
from weather.serializers import WeatherSerializer, WeatherStationSerializer

import pandas as pd

def home(request):
    df = pd.read_csv("./122_Alsheim_2018.csv")
    qs = Weather.objects.all()
    data = pd.DataFrame(qs)
    print(data)
    #df = df[:10]
    #print(df)
    mydict = {
        "qs": qs,
        "df": df,
        "hf": df.to_html()
    }
    return render(request, 'weather/main.html', mydict)

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post', 'put', 'delete'], renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        weather = self.get_object()
        return Response(weather.highlighted)

    def perform_create(self, serializer):
        serializer.save()

    

class WeatherStationViewSet(viewsets.ModelViewSet):
    queryset = WeatherStation.objects.all()
    serializer_class = WeatherStationSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post', 'put', 'delete'], renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        weatherStation = self.get_object()
        return Response(weatherStation.highlighted)

    def perform_create(self, serializer):
        serializer.save()
