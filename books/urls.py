from rest_framework.routers import DefaultRouter

from books.apps import BooksConfig
from books.views import BooksViewSet, AuthorViewSet, BookIssuanceViewSet

app_name = BooksConfig.name

router = DefaultRouter()
router.register(r"books", BooksViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"issuance", BookIssuanceViewSet)

urlpatterns = router.urls
