from django.test import TestCase
from apps.user.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.books_url = reverse('core:book:v1:books-list')

        # Create a test user for authentication
        self.user = User.objects.create(first_name='Test', last_name='User', email='testuser@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_and_list_books(self):
        # Create a book
        create_data = {'title': 'Test Book', 'isbn': '1234567890123', 'publication_year': 2022, 'brief_summary': 'A test book.'}
        response = self.client.post(self.books_url, data=create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # List books
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Book')

    def test_update_and_delete_book(self):
        # Create a book
        create_data = {'title': 'Test Book', 'isbn': '1234567890123', 'publication_year': 2022, 'brief_summary': 'A test book.'}
        response = self.client.post(self.books_url, data=create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        book_id = response.data['id']
        update_data = {'title': 'Updated Test Book', 'brief_summary': 'An updated test book.'}

        # Update the book
        response = self.client.patch(reverse('core:book:v1:books-detail', args=[book_id]), data=update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Test Book')

        # Delete the book
        response = self.client.delete(reverse('core:book:v1:books-detail', args=[book_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
