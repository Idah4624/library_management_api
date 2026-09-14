from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


def home(request):
    return JsonResponse({
        "message": "Library Management API",
        "version": "1.0.0",
        "docs": "/api/docs/"
    })


urlpatterns = [

    path("", home),

    path("admin/", admin.site.urls),

    path("api/accounts/", include("accounts.urls")),

    path("api/books/", include("books.urls")),

    path("api/borrowings/", include("borrowings.urls")),

    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]