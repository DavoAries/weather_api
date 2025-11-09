from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import CityTemperature
from .serializers import CityTemperatureSerializer

class CityTemperatureViewSet(viewsets.ModelViewSet):
    queryset = CityTemperature.objects.all()
    serializer_class = CityTemperatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

