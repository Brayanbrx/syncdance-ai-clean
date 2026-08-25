from rest_framework import permissions, viewsets

from common.permissions import IsInstructorOrAdmin

from .models import Routine
from .selectors import get_routines_for_user
from .serializers import RoutineSerializer
from .services import create_routine, update_routine


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    def get_queryset(self):
        return get_routines_for_user(user=self.request.user)

    def get_permissions(self):
        if self.action in {"list", "retrieve"}:
            return [permissions.IsAuthenticated()]
        return [IsInstructorOrAdmin()]

    def perform_create(self, serializer):
        serializer.instance = create_routine(
            instructor=self.request.user,
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_routine(
            routine=serializer.instance,
            **serializer.validated_data,
        )
