from django.urls import path
from . import views

urlpatterns = [
    path('api/v0/libraries/', views.get_all_libraries, name='get_all_libraries'),
    path('api/v0/libraries/<int:library_id>/', views.get_a_library, name='get_a_library'),
]
