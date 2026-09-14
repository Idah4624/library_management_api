from rest_framework import serializers

from .models import Borrowing


class BorrowingSerializer(
    serializers.ModelSerializer
):

    borrower_username = serializers.CharField(
        source="borrower.username",
        read_only=True
    )

    book_title = serializers.CharField(
        source="book.title",
        read_only=True
    )

    class Meta:

        model = Borrowing

        fields = (
            "id",
            "borrower",
            "borrower_username",
            "book",
            "book_title",
            "borrowed_at",
            "returned",
            "returned_at",
        )

        read_only_fields = (
            "borrower",
            "borrowed_at",
            "returned",
            "returned_at",
        )