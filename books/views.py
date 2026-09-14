from rest_framework import filters
from rest_framework.permissions import (
    IsAuthenticated,
    SAFE_METHODS,
)
from rest_framework.viewsets import (
    ModelViewSet
)

from accounts.permissions import (
    IsLibrarianOrAdmin
)

from .models import Book
from .serializers import (
    BookSerializer
)


class BookViewSet(
    ModelViewSet
):

    queryset = Book.objects.all().order_by(
        "-created_at"
    )

    serializer_class = BookSerializer

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        "title",
        "author",
        "isbn"
    ]

    def get_permissions(self):

        if self.request.method in SAFE_METHODS:
            return [
                IsAuthenticated()
            ]

        return [
            IsLibrarianOrAdmin()
        ]