import pytest
from rest_framework.test import APIClient

from apps.accounts.models import User


@pytest.mark.django_db
def test_instructor_can_create_routine():
    instructor = User.objects.create_user(
        username="instructor",
        email="instructor@example.com",
        password="password-123",
        role=User.Role.INSTRUCTOR,
    )
    client = APIClient()
    client.force_authenticate(instructor)

    response = client.post(
        "/api/routines/",
        {"name": "Rutina demo", "difficulty": "BEGINNER"},
        format="json",
    )

    assert response.status_code == 201
    assert response.data["instructor"] == "instructor"
