from apps.core.mixins import CustomModelSerializer

from apps.book.models import Book
from apps.user.api.v1.serializers import UserSerializer


class BookListSerializer(CustomModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'publication_year', 'author', 'created_at', 'updated_at')


class BookDetailsSerializer(CustomModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Book
        read_only_fields = ('id', 'author', 'created_at', 'updated_at')
        fields = ('title', 'isbn', 'publication_year', 'brief_summary') + read_only_fields
