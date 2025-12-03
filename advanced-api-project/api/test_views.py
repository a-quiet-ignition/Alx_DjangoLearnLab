from django.test import TestCase, APITestCase
from rest_framework import status
from .models import Book


class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            publication_year=2023,
            isbn="1234567890123"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.publication_year, 2023)
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_str_method(self):
        self.assertEqual(str(self.book), "Test Book by Test Author")
        
class BookViewTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="View Test Book",
            author="View Test Author",
            publication_year=2022,
        )

    def test_book_list_view(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Book")

    def test_book_detail_view(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Author")
        
    def test_book_create_view(self):
        response = self.client.post('/api/books/', {
            'title': "New Book",
            'author': "New Author",
            'publication_year': 2021,
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)
        
    def test_book_update_view(self):
        response = self.client.put(f'/api/books/{self.book.id}/', {
            'title': "Updated Book",
            'author': "Updated Author",
            'publication_year': 2020,
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")
        
    def test_book_delete_view(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Book.objects.count(), 0)
        
    
class BookAPITest(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="API Test Book",
            author="API Test Author",
            publication_year=2020,
        )
        
    def test_book_list_api(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_book_detail_api(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "API Test Book")
        
    def test_book_create_api(self):
        response = self.client.post('/api/books/', {
            'title': "API Created Book",
            'author': "API Created Author",
            'publication_year': 2019,
        })     
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        
    def test_book_update_api(self):
        response = self.client.put(f'/api/books/{self.book.id}/', {
            'title': "API Updated Book",
            'author': "API Updated Author",
            'publication_year': 2018,
        }, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "API Updated Book")
    