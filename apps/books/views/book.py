from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

from apps.books.models import Book
from apps.books.serializers.book import BookSerializer
from apps.paginations import PageNumberPagination
from apps.paginations import PageNumberPagination


class BookViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('author', 'language')
    ordering_fields = ('published_date',)
    ordering = ('published_date',)
    pagination_class = PageNumberPagination
