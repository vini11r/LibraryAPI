from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from books.models import BookIssuance
from books.serializers import BookDetailIssuanceSerializer
from users.models import User
from users.validators import user_password


class UserSerializer(serializers.ModelSerializer):
    books = SerializerMethodField()

    def get_books(self, user):
        queryset = BookIssuance.objects.filter(user=user.pk, returned=False)
        return [a.book.title for a in queryset]

    class Meta:
        model = User
        fields = ("id", "email", "phone", "first_name", "last_name", "books")


class UserDetailsSerializer(serializers.ModelSerializer):
    books = BookDetailIssuanceSerializer(source="bookissuance_set", many=True)

    class Meta:
        model = User
        fields = ("id", "email", "phone", "first_name", "last_name", "books")


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password", "phone", "first_name", "last_name")
        validators = [
            user_password,
        ]
