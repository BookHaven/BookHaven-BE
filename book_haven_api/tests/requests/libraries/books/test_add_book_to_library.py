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

    return library1


@pytest.mark.django_db
def test_add_book_to_library(Libraries):
    print('add_book_to_library_happy_path')
    library1 = Libraries
    url = reverse('get_library_books', kwargs={'library_id': library1.id})
    client = APIClient()
    response = client.post(url, {'isbn': '9780446675505'}, format='json')
    assert response.status_code == 201
    assert type(response.json()) is dict
    assert type(response.json()['data']) is dict
    attrs = response.json()['data']['attributes']
    assert type(attrs) is dict
    assert attrs['isbn'] == '9780446675505'
    assert attrs['book_image'] == 'http://books.google.com/books/content?id=OemtHIwYk0wC&printsec=frontcover&img=1&zoom=1&source=gbs_api'
    assert attrs['description'] == 'In a futuristic society filled with chaos, young Lauren Olamina begins a journey that will test her will and ultimately start a new faith. Includes questions for discussion.'
    assert attrs['title'] == 'Parable of the Sower'
    assert attrs['author'] == 'Octavia E. Butler'
    assert attrs['genre'] == 'FICTION'
    assert attrs['library_id'] == 1
    assert library1.book_set.count() == 1

@pytest.mark.django_db
def test_add_book_to_library_invalid_isbn(Libraries):
    print('add_book_to_library_sad_path_invalid_isbn')
    library1 = Libraries
    url = reverse('get_library_books', kwargs={'library_id': library1.id})
    client = APIClient()
    response = client.post(url, {'isbn': '978044667550'}, format='json')
  
    assert response.status_code == 422
    assert type(response.json()) is dict
    assert type(response.json()['errors']) is list
    assert type(response.json()['errors'][0]) is dict
    assert response.json()['errors'][0]['status'] == '422'
    assert response.json()['errors'][0]['title'] == 'Book not created'
    assert response.json()['errors'][0]['detail'] == 'Book could not be created because ISBN not found.'
    assert library1.book_set.count() == 0

    
