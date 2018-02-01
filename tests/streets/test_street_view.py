import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestStreetView(APITestCase):
    @pytest.mark.django_db
    def test_returns_street_list(self):
        # Need to figure out how to test view sets... 
        url = reverse('')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
