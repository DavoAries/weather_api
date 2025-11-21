from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from rest_framework.authtoken.views import obtain_auth_token  
from temperatures.views import CityTemperatureViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'temperatures', CityTemperatureViewSet, basename='temperature')

schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",
        default_version='v1',
        description="Documentación de la API de temperaturas",
        contact=openapi.Contact(email="tuemail@ejemplo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),

    # Esquema JSON
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Swagger UI y Redoc (usarán nuestras plantillas locales)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]








