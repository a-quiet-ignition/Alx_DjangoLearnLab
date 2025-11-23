from rest_framework import serializers
from .models import Book 

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
        