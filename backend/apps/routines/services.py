from .models import Routine


def create_routine(*, instructor, **validated_data) -> Routine:
    return Routine.objects.create(instructor=instructor, **validated_data)


def update_routine(*, routine: Routine, **validated_data) -> Routine:
    for field, value in validated_data.items():
        setattr(routine, field, value)
    routine.save()
    return routine
