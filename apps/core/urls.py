from django.http import HttpResponse
from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path("", lambda req: HttpResponse("Welcome to Digital Library API!"), name='api_home'),
    path("", include("apps.authentication.urls", namespace="authentication")),
    path("", include("apps.user.urls", namespace="user")),
    path("", include("apps.book.urls", namespace="book")),
]
