from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from utils.constants import DEVELOPMENT, LOCAL
from config.settings import ENVIRONMENT_NAME


def swagger_api_urlpatterns():
    schema_view = get_schema_view(
        openapi.Info(
            title="Digital Library Management System",
            default_version='v1',
            description='This repository contains the Django backend for a full-stack digital library management system. '
                        'The backend serves as a RESTful API, handling data operations for book records. The system includes'
                        ' a PostgreSQL database for storing book records.',
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="abdullah.2010bd@gmail.com"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny, ]
    )
    swagger_url = []

    if ENVIRONMENT_NAME in [LOCAL, DEVELOPMENT]:
        swagger_url += [
            path('api/v1/doc/sw/', schema_view.with_ui('swagger', cache_timeout=0)),
            path('api/v1/doc/re/', schema_view.with_ui('redoc', cache_timeout=0)),
        ]
    return swagger_url
