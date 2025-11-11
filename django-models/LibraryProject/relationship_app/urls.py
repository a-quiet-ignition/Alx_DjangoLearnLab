from django.urls import path
from . import views

urlpatterns = [
    path('list_book/', views.list_book, name='list_book'),
    path('library_detail/', views.LibraryDetailView.as_view(), name='library_detail'),
]