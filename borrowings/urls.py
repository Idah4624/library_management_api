from django.urls import path

from .views import (
    BorrowBookView,
    ReturnBookView,
    BorrowingHistoryView,
)

urlpatterns = [

    path(
        "borrow/<int:book_id>/",
        BorrowBookView.as_view(),
        name="borrow-book"
    ),

    path(
        "return/<int:borrowing_id>/",
        ReturnBookView.as_view(),
        name="return-book"
    ),

    path(
        "history/",
        BorrowingHistoryView.as_view(),
        name="history"
    ),
]