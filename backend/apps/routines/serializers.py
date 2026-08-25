from rest_framework import serializers

from .models import Routine


class RoutineSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Routine
        fields = (
            "id",
            "name",
            "description",
            "instructor",
            "difficulty",
            "master_video",
            "is_active",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "instructor", "created_at", "updated_at")
