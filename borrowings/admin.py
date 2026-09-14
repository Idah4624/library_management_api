from django.contrib import admin

from .models import Borrowing


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "borrower",
        "book",
        "borrowed_at",
        "returned",
    )

    list_filter = (
        "returned",
    )