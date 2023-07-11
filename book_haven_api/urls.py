from django.urls import path
from . import views

urlpatterns = [
    path('libraries/', views.get_all_libraries, name='get_all_libraries'),
]
