from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from books.models import BookIssuance
from books.serializers import BookDetailIssuanceSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    books = SerializerMethodField()

    def get_books(self, user):
        queryset = BookIssuance.objects.filter(user=user.pk)
        return [a.book.title for a in queryset]

    class Meta:
        model = User
        fields = ("id", "email", "phone", "first_name", "last_name", "books")


class UserDetailsSerializer(serializers.ModelSerializer):
    books = BookDetailIssuanceSerializer(source="bookissuance_set", many=True)

    class Meta:
        model = User
        fields = ("id", "email", "phone", "first_name", "last_name", "books")
