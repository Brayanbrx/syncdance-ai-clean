from django.urls import path

from .views import PerformanceAnalysisView

urlpatterns = [
    path(
        "<int:performance_id>/analysis/", PerformanceAnalysisView.as_view(), name="analysis-detail"
    )
]
