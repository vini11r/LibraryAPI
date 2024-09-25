from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from books.models import Books, Author, BookIssuance
from books.serializers import (
    BooksSerializer,
    AuthorSerializer,
    BookIssuanceSerializer,
    BookDetailsSerializer,
    AuthorDetailsSerializer,
)


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return BookDetailsSerializer
        return BooksSerializer

    # def retrieve(self, request, pk=None, **kwargs):
    #     queryset = Books.objects.all().filter(pk=pk)
    #     serializer = BookDetailsSerializer(queryset, many=True)
    #     return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AuthorDetailsSerializer
        return AuthorSerializer

    # def retrieve(self, request, pk=None, **kwargs):
    #     queryset = Author.objects.all().filter(pk=pk)
    #     serializer = AuthorDetailsSerializer(queryset, many=True)
    #     return Response(serializer.data)


class BookIssuanceViewSet(ModelViewSet):
    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer

    def perform_create(self, serializer):
        issuance = BookIssuance.objects.all().filter(returned=False)
        book_id = serializer.validated_data['book']
        if issuance.filter(book_id=book_id).exists() is False:
            serializer.save()
        else:
            raise ValidationError ("Эта книга еще не возвращена")






