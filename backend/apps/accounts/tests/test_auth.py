import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_and_login():
    client = APIClient()
    payload = {
        "username": "student01",
        "email": "student@example.com",
        "password": "safe-password-123",
    }

    register_response = client.post(reverse("register"), payload, format="json")
    login_response = client.post(
        reverse("login"),
        {"username": payload["username"], "password": payload["password"]},
        format="json",
    )

    assert register_response.status_code == 201
    assert login_response.status_code == 200
    assert "access" in login_response.data
