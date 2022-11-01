from django.urls import path, include

from weather import views
from rest_framework import routers


from rest_framework.urlpatterns import format_suffix_patterns
"""
urlpatterns = format_suffix_patterns([
    path('weather/', views.WeatherViewSet, name='weather'),
    path('weatherStation/', views.WeatherStationViewSet, name='weatherStation'),    
])"""

from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'weather', views.WeatherViewSet,basename="weather")
router.register(r'weatherStation', views.WeatherStationViewSet, basename="weatherStation")
#router.register(r'home', views.HomeViewSet,basename="home")


urlpatterns = [
    path('', include(router.urls)),
    path('home/' , views.home, name="home")
]