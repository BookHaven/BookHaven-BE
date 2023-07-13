import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from book_haven_api.models import Library, Book

@pytest.fixture
def libraries():
    library_1 =  Library.objects.create(
        name='Library1',
        street='1234 Library1 St.',
        city='Library1 City',
        state='CA',
        zip='12345',
        lat=123.456,
        lon=123.456,
    )
    library_2 = Library.objects.create(
        name='Library2',
        street='1234 Library2 St.',
        city='Library2 City',
        state='CA',
        zip='12345',
        lat=123.456,
        lon=123.456,
    )
  
    return library_1, library_2

@pytest.fixture
def Books(libraries):
    library_1, library_2 = libraries
    book1 = Book.objects.create(
        isbn='1234567890123',
        book_image='https://bookhaven.com/book1.jpg',
        description='This is book1',
        title='Book1',
        author='Author1',
        genre='Genre1',
        library=library_1,
    )
    book2 = Book.objects.create(
        isbn='1234567890124',
        book_image='https://bookhaven.com/book2.jpg',
        description='This is book2',
        title='Book2',
        author='Author2',
        genre='Genre2',
        library=library_1,
    )
    book3 = Book.objects.create(
        isbn='1234567890125',
        book_image='https://bookhaven.com/book3.jpg',
        description='This is book3',
        title='Book3',
        author='Author3',
        genre='Genre3',
        library=library_2,
    )
    return book1, book2, book3

@pytest.mark.django_db
def test_destroy_book(libraries, Books):
    print('test_destroy_book')
    library_1, library_2 = libraries
    book1, book2, book3 = Books
    client = APIClient()
    url = reverse('destroy_book', kwargs={'library_id': library_1.id, 'book_id': book1.id})
    response = client.delete(url)
    assert response.status_code == 204
    assert Book.objects.count() == 2
    assert Book.objects.filter(id=book1.id).count() == 0
    assert Book.objects.filter(id=book2.id).count() == 1
    assert Book.objects.filter(id=book3.id).count() == 1

@pytest.mark.django_db
def test_destroy_book_sad(libraries):
    print('test_destroy_book_sad')
    library_1, library_2 = libraries
    client = APIClient()
    url = reverse('destroy_book', kwargs={'library_id': library_1.id, 'book_id': 1})
    response = client.delete(url)
    assert response.status_code == 404
    assert type(response.json()) is dict
    assert 'errors' in response.json()
    assert type(response.json()['errors']) is list
    assert len(response.json()['errors']) == 1
    assert type(response.json()['errors'][0]) is dict
    assert 'status' in response.json()['errors'][0]
    assert 'title' in response.json()['errors'][0]
    assert 'detail' in response.json()['errors'][0]
    assert response.json()['errors'][0]['status'] == '404'
    assert response.json()['errors'][0]['title'] == 'Book not found'
    assert response.json()['errors'][0]['detail'] == 'The book with id 1 does not exist.'  # noqa: E501
