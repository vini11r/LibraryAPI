from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Author, BookIssuance, Books
from users.models import User


class BookTestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Test", last_name="Test")
        self.data = {
            "title": "Test Book",
            "author": self.author.pk,
            "publication_year": 2021,
            "genre": "Test Genre",
        }
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword123"
        )

    def test_create_book(self):
        url = reverse("books:books-list")
        self.client.force_authenticate(user=self.user)
        self.user.groups.create(name="Библиотекарь")
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_books(self):
        url = reverse("books:books-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        book = Books.objects.create(
            title="Test",
        )
        url = reverse("books:books-detail", args=(book.id,))
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        book = Books.objects.create(
            title="Test",
        )
        self.user.groups.create(name="Библиотекарь")
        url = reverse("books:books-detail", args=(book.id,))
        data = {"title": "Updated Test Book"}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        book = Books.objects.create(
            title="Test",
        )
        self.user.groups.create(name="Библиотекарь")
        url = reverse("books:books-detail", args=(book.id,))
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AuthorTestCase(APITestCase):
    def setUp(self):
        self.data = {
            "first_name": "Test",
            "last_name": "Test",
        }
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword123"
        )

    def test_create_author(self):
        url = reverse("books:author-list")
        self.client.force_authenticate(user=self.user)
        self.user.groups.create(name="Библиотекарь")
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_author(self):
        url = reverse("books:author-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_author(self):
        author = Author.objects.create(first_name="Test", last_name="Test")
        url = reverse("books:author-detail", args=(author.id,))
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_author(self):
        author = Author.objects.create(first_name="Test", last_name="Test")
        self.user.groups.create(name="Библиотекарь")
        url = reverse("books:author-detail", args=(author.id,))
        data = {"first_name": "Updated Test", "last_name": "Updated Test"}
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_author(self):
        author = Author.objects.create(first_name="Test", last_name="Test")
        self.user.groups.create(name="Библиотекарь")
        url = reverse("books:author-detail", args=(author.id,))
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookIssuanceTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword123"
        )
        self.book = Books.objects.create(
            title="Test",
        )

    def test_create_issuance(self):
        url = reverse("books:bookissuance-list")
        self.client.force_authenticate(user=self.user)
        self.user.groups.create(name="Библиотекарь")
        data = {"book": self.book.id, "user": self.user.id, "due_date": "2024-12-31"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_issuance_no_returned(self):
        url = reverse("books:bookissuance-list")
        self.client.force_authenticate(user=self.user)
        self.user.groups.create(name="Библиотекарь")
        data = {"book": self.book.id, "user": self.user.id, "due_date": "2024-12-31"}
        BookIssuance.objects.create(
            book=self.book, user=self.user, due_date="2024-12-31", returned=False
        )
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_issuance(self):
        issuance = BookIssuance.objects.create(
            book=self.book, user=self.user, due_date="2024-12-31"
        )
        url = reverse("books:bookissuance-detail", args=(issuance.id,))
        self.user.groups.create(name="Библиотекарь")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_issuance(self):
        issuance = BookIssuance.objects.create(
            book=self.book, user=self.user, due_date="2024-12-31"
        )
        url = reverse("books:bookissuance-detail", args=(issuance.id,))
        self.user.groups.create(name="Библиотекарь")
        self.client.force_authenticate(user=self.user)
        data = {"user": self.user.id, "book": self.book.id, "due_date": "2025-12-31"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_issuance(self):
        issuance = BookIssuance.objects.create(
            book=self.book, user=self.user, due_date="2024-12-31"
        )
        url = reverse("books:bookissuance-detail", args=(issuance.id,))
        self.user.groups.create(name="Библиотекарь")
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
