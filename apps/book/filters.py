import django_filters.rest_framework as filters

from apps.book.models import Book


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'publication_year', 'author')
