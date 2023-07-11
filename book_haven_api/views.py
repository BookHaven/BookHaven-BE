from .models import Library, Book
from .serializers import LibrarySerializer, BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

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
    
@api_view(['GET'])
def get_library_books(request, library_id):
    library = Library.objects.get(id=library_id)
    books = library.book_set
    serializer = BookSerializer(books, many=True)
    return Response({ "data": serializer.data }, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def destroy_book(request, library_id, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({"errors": [{
            "status": "404",
            "title": "Book not found",
            "detail": "The book with id " + str(book_id) + " does not exist."
        }]},status=status.HTTP_404_NOT_FOUND)