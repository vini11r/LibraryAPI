from rest_framework import serializers

from books.models import Books, Author, BookIssuance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("pk", "first_name", "last_name",)

class BooksSerializer(serializers.ModelSerializer):
    book_author = AuthorSerializer(source="author", many=True)
    class Meta:
        model = Books
        fields = "__all__"

class BookIssuanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssuance
        fields = "__all__"