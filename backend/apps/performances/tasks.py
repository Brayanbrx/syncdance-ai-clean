import time

from celery import shared_task


@shared_task(bind=True, max_retries=2)
def analyze_performance(self, performance_id: int):
    from apps.analysis.services import complete_analysis

    from .models import Performance

    performance = Performance.objects.get(pk=performance_id)
    performance.status = Performance.Status.PROCESSING
    performance.save(update_fields=("status", "updated_at"))

    try:
        time.sleep(1)
        complete_analysis(performance=performance)
    except Exception:
        performance.status = Performance.Status.FAILED
        performance.save(update_fields=("status", "updated_at"))
        raise
