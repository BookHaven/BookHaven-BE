from django.urls import path
from . import views

urlpatterns = [
    path('api/v0/libraries/', views.get_all_libraries, name='get_all_libraries'),
    path('api/v0/libraries/<int:library_id>/', views.get_a_library, name='get_a_library'),  # noqa: E501
    path('api/v0/libraries/<int:library_id>/books/', views.get_library_books, name='get_library_books'),  # noqa: E501
    path('api/v0/libraries/<int:library_id>/books/<int:book_id>', views.destroy_book, name='destroy_book'),  # noqa: E501
]
