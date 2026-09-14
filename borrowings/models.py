from django.db import models
from django.conf import settings

from books.models import Book


class Borrowing(models.Model):

    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="borrowings"
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="borrowings"
    )

    borrowed_at = models.DateTimeField(
        auto_now_add=True
    )

    returned_at = models.DateTimeField(
        null=True,
        blank=True
    )

    returned = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.borrower.username} borrowed {self.book.title}"