from django.shortcuts import render
from .models import Library
from .serializers import LibrarySerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_all_libraries(request):
    libraries = Library.objects.all()
    serializer = LibrarySerializer(libraries, many=True)
    return Response({ "data": serializer.data }, status=status.HTTP_200_OK)
