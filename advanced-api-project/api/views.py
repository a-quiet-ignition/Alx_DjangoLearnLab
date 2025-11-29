from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
# Generic Views for Book Model
class BookListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
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
    
