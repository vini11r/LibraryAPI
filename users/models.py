from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, max_length=255, verbose_name="Почта", help_text="Укажите почту"
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name="Имя",
        help_text="Введите имя",
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name="Фамилия",
        help_text="Введите фамилию",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
