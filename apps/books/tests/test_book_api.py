from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.books.models import Book
from apps.books.tests.factories import BookFactory


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.book1 = BookFactory()
        self.book2 = BookFactory()

    def test_create_book(self):
        url = reverse('books:book-list')
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2024-08-01',
            'isbn': '1234567890124',
            'pages': 200,
            'cover': 'https://example.com/cover.jpg',
            'language': 'English',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_list_books(self):
        url = reverse('books:book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_retrieve_book(self):
        url = reverse('books:book-detail', args=[self.book1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        url = reverse('books:book-detail', args=[self.book1.id])
        data = {
            'title': 'Updated Title',
            'author': self.book1.author,
            'published_date': self.book1.published_date,
            'isbn': self.book1.isbn,
            'pages': self.book1.pages,
            'cover': self.book1.cover,
            'language': self.book1.language,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        url = reverse('books:book-detail', args=[self.book1.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        url = reverse('books:book-list') + f'?search={self.book1.author}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['author'], self.book1.author)

    def test_filter_books_by_language(self):
        url = reverse('books:book-list') + f'?search={self.book1.language}'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['language'], self.book1.language)

    def test_pagination(self):
        for _ in range(12):
            BookFactory()

        url = reverse('books:book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

        url = reverse('books:book-list') + '?page=2'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 4)
