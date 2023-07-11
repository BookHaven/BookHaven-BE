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
def test_get_a_library_happy(Libraries, Books):
    print('test_get_a_library')
    client = APIClient()
    url = reverse('get_a_library', kwargs={'library_id': 1})
    response = client.get(url)

    assert response.status_code == 200
    assert type(response.json()) is dict
    assert 'data' in response.json()

    assert type(response.json()['data']) is dict
    assert 'id' in response.json()['data']
    assert 'type' in response.json()['data']
    assert 'attributes' in response.json()['data']
    assert 'name' in response.json()['data']['attributes']

    address_attributes = response.json()['data']['attributes']['address']

    assert type(address_attributes) is dict
    assert 'street' in address_attributes
    assert 'city' in address_attributes
    assert 'state' in address_attributes
    assert 'zip' in address_attributes

    location_attributes = response.json()['data']['attributes']['location']

    assert type(location_attributes) is dict
    assert 'lat' in location_attributes
    assert 'lon' in location_attributes



@pytest.mark.django_db
def test_get_a_library_sad(Libraries, Books):
    print('test_get_a_library_sad')
    client = APIClient()
    url = reverse('get_a_library', kwargs={'library_id': 5})
    response = client.get(url)

    # breakpoint()
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
    assert response.json()['errors'][0]['title'] == 'Library not found'
    assert response.json()['errors'][0]['detail'] == 'The library with id 5 does not exist.'