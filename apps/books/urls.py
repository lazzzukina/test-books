from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.books.views.book import BookViewSet

app_name = 'books'

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
