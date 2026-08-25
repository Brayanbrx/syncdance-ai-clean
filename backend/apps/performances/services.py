from rest_framework.exceptions import ValidationError

from .models import Performance
from .tasks import analyze_performance


def upload_performance(*, student, **validated_data) -> Performance:
    return Performance.objects.create(student=student, **validated_data)


def request_analysis(*, performance: Performance) -> Performance:
    if performance.status not in {Performance.Status.UPLOADED, Performance.Status.FAILED}:
        raise ValidationError({"status": "La performance ya fue enviada a análisis."})

    performance.status = Performance.Status.QUEUED
    performance.save(update_fields=("status", "updated_at"))
    analyze_performance.delay(performance.pk)
    return performance
