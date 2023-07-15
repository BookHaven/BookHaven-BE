from .models import Library, Book
from .serializers import LibrarySerializer, BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
from decouple import config

# Create your views here.
@api_view(['GET'])
def get_all_libraries(request):
    libraries = Library.objects.all()
    serializer = LibrarySerializer(libraries, many=True)
    return Response({ "data": serializer.data }, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_a_library(request, library_id):
    try :
        library = Library.objects.get(id=library_id)
        serializer = LibrarySerializer(library, many=False)
        return Response({ "data": serializer.data }, status=status.HTTP_200_OK)
    except Library.DoesNotExist:
        return Response({"errors": [{
            "status": "404",
            "title": "Library not found",
            "detail": "The library with id " + str(library_id) + " does not exist."
        }]},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET', 'POST'])
def get_library_books(request, library_id):
    if request.method == 'GET':
        library = Library.objects.get(id=library_id)
        books = library.book_set
        serializer = BookSerializer(books, many=True)
        return Response({ "data": serializer.data }, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        library = Library.objects.get(id=library_id)
        api_key = config('MY_API_KEY')
        url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + request.data['isbn'] + '&key=' + api_key
        response = requests.get(url)
        if response.json()['totalItems'] == 0:
            return Response({"errors": [{
                "status": "422",
                "title": "Book not created",
                "detail": "Book could not be created because ISBN not found."
            }]},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        book = Book.objects.create(
            isbn=request.data['isbn'],
            book_image=response.json()['items'][0]['volumeInfo']['imageLinks']['thumbnail'],
            description=response.json()['items'][0]['volumeInfo']['description'],
            title=response.json()['items'][0]['volumeInfo']['title'],
            author=response.json()['items'][0]['volumeInfo']['authors'][0],
            genre=response.json()['items'][0]['volumeInfo']['categories'][0],
            library=library,
        )
        serializer = BookSerializer(book, many=False)
        return Response({ "data": serializer.data }, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def destroy_book(request, library_id, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response({ "data": {
            "id": book_id,
            "detail": "The book with id " + str(book_id) + " was deleted."
        }},status=status.HTTP_200_OK )
    except Book.DoesNotExist:
        return Response({"errors": [{
            "status": "404",
            "title": "Book not found",
            "detail": "The book with id " + str(book_id) + " does not exist."
        }]},status=status.HTTP_404_NOT_FOUND)
