from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_book, name='list_books'),
    path('library_detail/', views.LibraryDetailView.as_view(), name='library_detail'),
]