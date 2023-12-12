from django.http import HttpResponse
from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path("", lambda req: HttpResponse("Welcome to Digital Library API!"), name='api_home'),
    path("", include("apps.book.urls", namespace="book")),
    path("", include("apps.user.urls", namespace="user")),
]
