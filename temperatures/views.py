from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import CityTemperature
from .serializers import CityTemperatureSerializer

# drf-yasg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CityTemperatureViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar temperaturas por ciudad.
    Endpoints disponibles:
    - /api/temperatures/ (GET, POST)
    - /api/temperatures/{id}/ (GET, PUT, PATCH, DELETE)
    """
    queryset = CityTemperature.objects.all()
    serializer_class = CityTemperatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Obtener lista de temperaturas registradas",
        responses={200: CityTemperatureSerializer(many=True)},
        examples={
            "application/json": [
                {"id": 1, "city": "Caracas", "temperature": "28°C"},
                {"id": 2, "city": "Maracaibo", "temperature": "31°C"}
            ]
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtener temperatura de una ciudad específica por ID",
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                description="ID del registro de temperatura",
                type=openapi.TYPE_INTEGER,
                required=True,
            )
        ],
        responses={200: CityTemperatureSerializer()},
        examples={
            "application/json": {"id": 1, "city": "Caracas", "temperature": "28°C"}
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Registrar una nueva temperatura para una ciudad",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['city', 'temperature'],
            properties={
                'city': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de la ciudad'),
                'temperature': openapi.Schema(type=openapi.TYPE_STRING, description='Temperatura (ej. 28°C)'),
            },
            example={"city": "Cumaná", "temperature": "29°C"}
        ),
        responses={201: CityTemperatureSerializer()},
        examples={
            "application/json": {"id": 3, "city": "Cumaná", "temperature": "29°C"}
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualizar la temperatura de una ciudad existente",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'city': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de la ciudad'),
                'temperature': openapi.Schema(type=openapi.TYPE_STRING, description='Temperatura (ej. 30°C)'),
            },
            example={"temperature": "30°C"}
        ),
        responses={200: CityTemperatureSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Eliminar un registro de temperatura por ID",
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                description="ID del registro a eliminar",
                type=openapi.TYPE_INTEGER,
                required=True,
            )
        ],
        responses={204: 'Registro eliminado correctamente'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




