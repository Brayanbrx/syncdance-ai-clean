from rest_framework import serializers

from .models import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Performance
        fields = ("id", "student", "routine", "video", "status", "created_at", "updated_at")
        read_only_fields = ("id", "student", "status", "created_at", "updated_at")


class PerformanceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ("id", "status", "updated_at")
