from rest_framework.serializers import ModelSerializer
from books.models import Book

# Task22: Create serializer for book
class BookSerializer(ModelSerializer):
    class Meta:
        # Define model
        model = Book
        # Define attributes to serialize
        fields = '__all__'
