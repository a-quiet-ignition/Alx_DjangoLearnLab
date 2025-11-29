from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend, filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
# Generic Views for Book Model
class BookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title' , 'publication_year']
    
class BookDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        serializer.save()
    
class BookUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_update(self, serializer):
        serializer.save()
    
class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
