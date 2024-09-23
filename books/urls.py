from rest_framework.routers import DefaultRouter

from books.apps import BooksConfig
from books.views import BooksViewSet, AuthorViewSet

app_name = BooksConfig.name

router = DefaultRouter()
router.register(r"books", BooksViewSet)
router.register(r"authors", AuthorViewSet)

urlpatterns = router.urls
