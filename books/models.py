from django.db import models


class Book(models.Model):

    title = models.CharField(
        max_length=255
    )

    author = models.CharField(
        max_length=255
    )

    isbn = models.CharField(
        max_length=20,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    total_copies = models.PositiveIntegerField(
        default=1
    )

    available_copies = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title