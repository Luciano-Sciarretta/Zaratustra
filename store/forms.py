from django.forms import ModelForm
from books.models import Book, Author
from django import forms

class UploadForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'stock_quantity',  'price', 'author', 'cover_image', 'synopsis', 'genre']
        widgets = {
            'author': forms.TextInput(),
        }

    
        