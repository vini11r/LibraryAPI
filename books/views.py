from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from books.models import Author, BookIssuance, Books
from books.serializers import (AuthorDetailsSerializer, AuthorSerializer,
                               BookDetailIssuanceSerializer,
                               BookDetailsSerializer, BookIssuanceSerializer,
                               BooksSerializer)
from config.settings import CACHE_ENABLED


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = [
        "author__last_name",
        "title",
        "genre",
    ]
    filterset_fields = (
        "title",
        "author",
        "genre",
    )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BookDetailsSerializer
        return BooksSerializer

    def get_queryset(self):
        if CACHE_ENABLED:
            key = f"books_list"
            books_list = cache.get(key)
            if books_list is None:
                books_list = Books.objects.all()
                cache.set(key, books_list)
        else:
            books_list = Books.objects.all()
        return books_list


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = [
        "first_name",
        "last_name",
    ]
    filterset_fields = (
        "first_name",
        "last_name",
    )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AuthorDetailsSerializer
        return AuthorSerializer


class BookIssuanceViewSet(ModelViewSet):
    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    ordering_fields = ["issue_date", "due_date"]
    search_fields = [
        "user__email",
        "book__title",
    ]
    filterset_fields = ("returned",)

    def perform_create(self, serializer):
        """
        Проверяем, возвращена ли книга.
        Если да, сохраняем выпуск.
        Если нет, выкидываем исключение.

        """
        issuance = BookIssuance.objects.all().filter(returned=False)
        book_id = serializer.validated_data["book"]
        if issuance.filter(book_id=book_id).exists() is False:
            serializer.save()
        else:
            raise ValidationError("Эта книга еще не возвращена")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BookDetailIssuanceSerializer
        return BookIssuanceSerializer
