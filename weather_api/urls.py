from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token  
from temperatures.views import CityTemperatureViewSet

router = routers.DefaultRouter()
router.register(r'temperatures', CityTemperatureViewSet, basename='temperature')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),  
]


