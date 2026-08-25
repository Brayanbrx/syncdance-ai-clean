from .models import Routine


def get_routines_for_user(*, user):
    queryset = Routine.objects.select_related("instructor")
    if not user.is_authenticated:
        return queryset.none()
    if user.role == user.Role.STUDENT:
        return queryset.filter(is_active=True)
    if user.role == user.Role.INSTRUCTOR:
        return queryset.filter(instructor=user)
    return queryset
