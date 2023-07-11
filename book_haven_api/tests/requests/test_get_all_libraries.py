import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from book_haven_api.models import Library, Book

@pytest.fixture
def Libraries():
    library1 =  Library.objects.create(
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
        library=library2,
    )
    return book1, book2

@pytest.mark.django_db
def test_get_all_libraries(Libraries, Books):
    print('test_get_all_libraries')
    client = APIClient()
    url = reverse('get_all_libraries') # from book_haven_api/urls.py
    response = client.get(url)

    assert response.status_code == 200
    assert Library.objects.count() == 2
    assert type(response.json()) is dict
    assert 'data' in response.json()
    assert type(response.json()['data']) is list

    for library in response.json()['data']:
        assert 'id' in library
        assert 'type' in library
        assert library['type'] == "library"
        assert 'attributes' in library
        assert 'name' in library['attributes']
        assert 'address' in library['attributes']
        assert type(library['attributes']['address']) is dict
        assert 'street' in library['attributes']['address']
        assert 'city' in library['attributes']['address']
        assert 'state' in library['attributes']['address']
        assert 'zip' in library['attributes']['address']
        assert 'location' in library['attributes']
        assert type(library['attributes']['location']) is dict
        assert 'lat' in library['attributes']['location']
        assert 'lon' in library['attributes']['location']
