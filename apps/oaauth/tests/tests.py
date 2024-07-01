import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient



@pytest.mark.django_db
def test_valid_shopping_list_is_created():
    url = reverse("login")
    data = {
        "username": "lisi",
        "password": "123456",
    }
    client = APIClient()
    response = client.post(url, data, fromat="json")
    assert response.status_code == status.HTTP_200_OK



