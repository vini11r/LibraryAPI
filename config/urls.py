from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls", namespace="books")),
    path("", include("users.urls", namespace="users")),
]
