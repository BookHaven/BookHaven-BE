from rest_framework.serializers import ModelSerializer
from .models import Library, Book

class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        new_representation = {
            'id': representation.get('id'),
            'type': 'library',
            'attributes': {
                'name': representation.get('name'),
                'address': {
                    'street': representation.get('street'),
                    'city': representation.get('city'),
                    'state': representation.get('state'),
                    'zip': representation.get('zip'),
                },
                'location': {
                    'lat': representation.get('lat'),
                    'lon': representation.get('lon'),
                },
                'book_count': instance.book_set.count(),
            }
        }
        return new_representation
    
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        new_representation = {
            'id': representation.get('id'),
            'type': 'book',
            'attributes': {
                'title': representation.get('title'),
                'author': representation.get('author'),
                'isbn': representation.get('isbn'),
                'book_image': representation.get('book_image'),
                'description': representation.get('description'),
                'genre': representation.get('genre'),
                'library_id': representation.get('library'),
            }
        }
        return new_representation
