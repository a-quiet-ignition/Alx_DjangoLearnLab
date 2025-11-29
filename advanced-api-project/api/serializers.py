from rest_framework import serializers
from .models import Author, Book

# Book Serializer with a publication year validator
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        
    def validate_publication_year(self, value):
        if value < 0 or value > 9999:
            raise serializers.ValidationError("Published year must be a valid year.")
        return value

# Author Serializer with a nested representation of books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['name', 'books']
        
        