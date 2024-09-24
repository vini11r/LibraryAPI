from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from books.models import Books, Author, BookIssuance
from books.serializers import BooksSerializer, AuthorSerializer, BookIssuanceSerializer, BookDetailsSerializer, AuthorDetailsSerializer


class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Books.objects.all().filter(pk=pk)
        serializer = BookDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Author.objects.all().filter(pk=pk)
        serializer = AuthorDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class BookIssuanceAPIView(APIView):
    queryset = BookIssuance.objects.all()
    serializer_class = BookIssuanceSerializer
