from .models import Performance


def get_performances_for_user(*, user):
    queryset = Performance.objects.select_related("student", "routine", "routine__instructor")
    if not user.is_authenticated:
        return queryset.none()
    if user.role == user.Role.STUDENT:
        return queryset.filter(student=user)
    if user.role == user.Role.INSTRUCTOR:
        return queryset.filter(routine__instructor=user)
    return queryset
