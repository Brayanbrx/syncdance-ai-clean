from .models import User


def register_user(**validated_data) -> User:
    return User.objects.create_user(role=User.Role.STUDENT, **validated_data)
