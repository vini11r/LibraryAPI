from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from books.models import Books, Author, BookIssuance
from books.serializers import BooksSerializer, AuthorSerializer, BookIssuanceSerializer


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookIssuanceAPIView(APIView):
    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer