from rest_framework import serializers

from books.models import Books, Author, BookIssuance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "pk",
            "first_name",
            "last_name",
        )


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


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
