from django.test import TestCase
from .models import CityTemperature

class CityTemperatureModelTest(TestCase):
    def test_create_city_temperature(self):
        temp = CityTemperature.objects.create(
            city="Cumaná",
            temperature=29.5
        )
        self.assertEqual(temp.city, "Cumaná")
        self.assertEqual(float(temp.temperature), 29.5)

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class CityTemperatureAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_create_temperature(self):
        data = {"city": "Caracas", "temperature": 30.0}
        response = self.client.post("/api/temperatures/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_temperatures(self):
        response = self.client.get("/api/temperatures/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

