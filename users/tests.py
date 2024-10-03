from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create(self):
        self.url = reverse("users:user-list")
        self.user_data = {
            "email": "testuser@example.com",
            "password": "testpassword123",
        }
        response = self.client.post(self.url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        self.url = reverse("users:user-list")
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword123"
        )
        self.client.force_authenticate(user=self.user)
        self.user.groups.create(name="Библиотекарь")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_user(self):
        self.url = reverse("users:user-list")
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword123"
        )
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update(self):
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword123"
        )
        self.url = reverse("users:user-detail", args=[self.user.id])
        self.user_data = {
            "email": "testuser2@example.com",
            "password": "testpassword1234",
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword123"
        )
        self.url = reverse("users:user-detail", args=[self.user.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        self.user = User.objects.create(
            email="testuser@example.com", password="testpassword123"
        )
        self.url = reverse("users:user-detail", args=[self.user.id])
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
