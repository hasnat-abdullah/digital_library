from rest_framework import permissions

from apps.core.mixins import CustomModelViewSet
from apps.core.permissions import IsBookOwner
from .serializers import BookListSerializer, BookDetailsSerializer
from apps.book.filters import BookFilter


class BookViewSet(CustomModelViewSet):
    serializer_class = BookDetailsSerializer
    serializer_classes_by_action = {"list": BookListSerializer}
    queryset = serializer_class.Meta.model.objects.all().order_by("title")
    lookup_field = "pk"
    filter_class = BookFilter
    search_fields = ("title",)
    permission_classes = [permissions.IsAuthenticated, ]
    permission_classes_by_action = {
        "list": [permissions.AllowAny],
        "retrieve": [permissions.AllowAny],
        "create": [IsBookOwner],
        "partial_update": [IsBookOwner],
        "destroy": [IsBookOwner]
    }
    ordering_fields = (
        "title",
        "isbn",
        "publication_year",
    )
    http_method_names = ["get", "post", "patch", 'delete']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
