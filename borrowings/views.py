from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from books.models import Book

from .models import Borrowing
from .serializers import (
    BorrowingSerializer
)


class BorrowBookView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        book_id
    ):

        try:

            book = Book.objects.get(
                id=book_id
            )

        except Book.DoesNotExist:

            return Response(
                {
                    "error":
                    "Book not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if book.available_copies <= 0:

            return Response(
                {
                    "error":
                    "No copies available"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        borrowing = Borrowing.objects.create(
            borrower=request.user,
            book=book
        )

        book.available_copies -= 1

        book.save()

        serializer = BorrowingSerializer(
            borrowing
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class ReturnBookView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(
        self,
        request,
        borrowing_id
    ):

        try:

            borrowing = Borrowing.objects.get(
                id=borrowing_id,
                borrower=request.user
            )

        except Borrowing.DoesNotExist:

            return Response(
                {
                    "error":
                    "Borrow record not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if borrowing.returned:

            return Response(
                {
                    "error":
                    "Book already returned"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        borrowing.returned = True

        borrowing.returned_at = timezone.now()

        borrowing.save()

        book = borrowing.book

        book.available_copies += 1

        book.save()

        return Response(
            {
                "message":
                "Book returned successfully"
            }
        )


class BorrowingHistoryView(
    ListAPIView
):

    serializer_class = (
        BorrowingSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return Borrowing.objects.filter(
            borrower=self.request.user
        ).order_by(
            "-borrowed_at"
        )