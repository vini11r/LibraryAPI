from django.contrib import admin

from books.models import Author, Books, BookIssuance

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(BookIssuance)
