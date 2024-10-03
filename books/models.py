from django.conf import settings
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя автора")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия автора")

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Books(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.ManyToManyField(
        Author, max_length=255, verbose_name="Автор", related_name="author_book"
    )
    publication_year = models.IntegerField(
        verbose_name="Год издания", blank=True, null=True
    )
    genre = models.CharField(max_length=255, verbose_name="Жанр", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookIssuance(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    book = models.ForeignKey(
        Books, on_delete=models.CASCADE, verbose_name="Выданная книга"
    )
    issue_date = models.DateField(auto_now_add=True, verbose_name="Дата выдачи")
    due_date = models.DateField(verbose_name="Дата возврата")
    returned = models.BooleanField(default=False, verbose_name="Возвращена")

    def __str__(self):
        return f"{self.user} - {self.book}"

    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдачи книг"
