from django.contrib import admin

from books.models import Author, BookIssuance, Books

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(BookIssuance)
