from rest_framework import serializers

from .models import Analysis


class AnalysisSerializer(serializers.ModelSerializer):
    performance_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Analysis
        fields = (
            "performance_id",
            "dance_score",
            "voice_score",
            "rhythm_score",
            "sync_score",
            "overall_score",
            "created_at",
        )
