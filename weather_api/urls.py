from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from temperatures.views import CityTemperatureViewSet

router = routers.DefaultRouter()
router.register(r'temperatures', CityTemperatureViewSet, basename='temperature')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]


