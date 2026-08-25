from django.shortcuts import get_object_or_404

from apps.performances.selectors import get_performances_for_user

from .models import Analysis


def get_analysis_result(*, user, performance_id: int) -> Analysis:
    performance = get_object_or_404(
        get_performances_for_user(user=user),
        pk=performance_id,
    )
    return get_object_or_404(Analysis, performance=performance)
