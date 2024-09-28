from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from books.models import Author, BookIssuance, Books


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "pk",
            "first_name",
            "last_name",
        )


class BooksSerializer(serializers.ModelSerializer):
    book_author = SerializerMethodField()

    def get_book_author(self, obj):
        return [author.last_name for author in obj.author.all()]

    class Meta:
        model = Books
        fields = (
            "id",
            "title",
            "publication_year",
            "genre",
            "description",
            "book_author",
        )


class AuthorDetailsSerializer(serializers.ModelSerializer):
    author_book = BooksSerializer(many=True)

    class Meta:
        model = Author
        fields = ("pk", "first_name", "last_name", "author_book")


class BookDetailsSerializer(serializers.ModelSerializer):
    book_author = AuthorSerializer(source="author", many=True, read_only=True)

    class Meta:
        model = Books
        fields = (
            "pk",
            "title",
            "book_author",
            "publication_year",
            "genre",
            "description",
        )


class BookIssuanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssuance
        fields = "__all__"


class BookDetailIssuanceSerializer(serializers.ModelSerializer):
    book = SerializerMethodField()
    user = SerializerMethodField()

    def get_book(self, obj):
        return f"Книга - {obj.book.title}, id книги - {obj.book.pk}"

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = BookIssuance
        fields = "__all__"
