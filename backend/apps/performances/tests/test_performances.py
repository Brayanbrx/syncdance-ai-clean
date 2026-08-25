from unittest.mock import patch

import pytest
from rest_framework.test import APIClient

from apps.accounts.models import User
from apps.routines.models import Routine


@pytest.mark.django_db
@patch("apps.performances.services.analyze_performance.delay")
def test_student_can_create_and_queue_performance(delay_mock):
    instructor = User.objects.create_user(
        username="instructor", email="teacher@example.com", role=User.Role.INSTRUCTOR
    )
    student = User.objects.create_user(
        username="student", email="student@example.com", role=User.Role.STUDENT
    )
    routine = Routine.objects.create(
        name="Demo", difficulty=Routine.Difficulty.BEGINNER, instructor=instructor
    )
    client = APIClient()
    client.force_authenticate(student)

    create_response = client.post("/api/performances/", {"routine": routine.pk}, format="json")
    analyze_response = client.post(f"/api/performances/{create_response.data['id']}/analyze/")

    assert create_response.status_code == 201
    assert analyze_response.status_code == 202
    assert analyze_response.data["status"] == "QUEUED"
    delay_mock.assert_called_once()
