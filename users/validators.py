from rest_framework.exceptions import ValidationError


def user_password(user):
    if user.get("password") is None:
        raise ValidationError("Пароль не может быть пустым")
