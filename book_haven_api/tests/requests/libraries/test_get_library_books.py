import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from book_haven_api.models import Library, Book

@pytest.fixture
def Libraries():
    library1 =  Library.objects.create(
        id=1,
        name='Library1',
        street='1234 Library1 St.',
        city='Library1 City',
        state='CA',
        zip='12345',
        lat=123.456,
        lon=123.456,
    )
    library2 = Library.objects.create(
        name='Library2',
        street='1234 Library2 St.',
        city='Library2 City',
        state='CA',
        zip='12345',
        lat=123.456,
        lon=123.456,
    )
  
    return library1, library2

@pytest.fixture
def Books(Libraries):
    library1, library2 = Libraries
    book1 = Book.objects.create(
        isbn='1234567890123',
        book_image='https://bookhaven.com/book1.jpg',
        description='This is book1',
        title='Book1',
        author='Author1',
        genre='Genre1',
        library=library1,
    )
    book2 = Book.objects.create(
        isbn='1234567890124',
        book_image='https://bookhaven.com/book2.jpg',
        description='This is book2',
        title='Book2',
        author='Author2',
        genre='Genre2',
        library=library1,
    )
    book3 = Book.objects.create(
        isbn='1234567890125',
        book_image='https://bookhaven.com/book3.jpg',
        description='This is book3',
        title='Book3',
        author='Author3',
        genre='Genre3',
        library=library2,
    )
    return book1, book2, book3

@pytest.mark.django_db
def test_get_library_books(Libraries, Books):
    print('test_get_library_books')
    client = APIClient()
    url = reverse('get_library_books', kwargs={'library_id': 1})
    # breakpoint()
    response = client.get(url)
    assert response.status_code == 200
    assert Book.objects.count() == 3
    assert type(response.json()) is dict
    assert 'data' in response.json()
    assert type(response.json()['data']) is list

    for book in response.json()['data']:
        assert 'id' in book
        assert 'type' in book
        assert book['type'] == "book"
        assert 'attributes' in book
        assert 'isbn' in book['attributes']
        assert 'book_image' in book['attributes']
        assert 'description' in book['attributes']
        assert 'title' in book['attributes']
        assert 'author' in book['attributes']
        assert 'genre' in book['attributes']
        assert 'library_id' in book['attributes']