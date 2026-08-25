from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .selectors import get_analysis_result
from .serializers import AnalysisSerializer


class PerformanceAnalysisView(generics.RetrieveAPIView):
    serializer_class = AnalysisSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_analysis_result(
            user=self.request.user,
            performance_id=self.kwargs["performance_id"],
        )
