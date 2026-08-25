from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Performance
from .selectors import get_performances_for_user
from .serializers import PerformanceSerializer, PerformanceStatusSerializer
from .services import request_analysis, upload_performance


class PerformanceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Performance.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PerformanceSerializer

    def get_queryset(self):
        return get_performances_for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.instance = upload_performance(
            student=self.request.user,
            **serializer.validated_data,
        )

    @action(detail=True, methods=["post"])
    def analyze(self, request, pk=None):
        performance = request_analysis(performance=self.get_object())
        return Response(
            PerformanceStatusSerializer(performance).data, status=status.HTTP_202_ACCEPTED
        )

    @action(detail=True, methods=["get"])
    def status(self, request, pk=None):
        return Response(PerformanceStatusSerializer(self.get_object()).data)
