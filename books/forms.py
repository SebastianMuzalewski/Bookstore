# Import ModelForm
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# Import book
from .models import Book

# Create book form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['posted_by', 'updated_at', 'created_at']
        