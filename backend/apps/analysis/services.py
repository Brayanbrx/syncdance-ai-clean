from decimal import Decimal

from apps.performances.models import Performance

from .models import Analysis


def complete_analysis(*, performance: Performance) -> Analysis:
    result, _ = Analysis.objects.update_or_create(
        performance=performance,
        defaults={
            "dance_score": Decimal("85.00"),
            "voice_score": Decimal("82.00"),
            "rhythm_score": Decimal("84.00"),
            "sync_score": Decimal("80.00"),
            "overall_score": Decimal("82.75"),
        },
    )
    performance.status = Performance.Status.COMPLETED
    performance.save(update_fields=("status", "updated_at"))
    return result
