from django.forms import ModelForm
from books.models import Book, Author
from django import forms

class UploadForm(ModelForm):
    author = forms.CharField(max_length=100)
    class Meta:
        model = Book
        fields = ['title', 'stock_quantity',  'price', 'author', 'cover_image', 'synopsis', 'genre']

    def clean_author(self):
        input = self.cleaned_data.get('author')
        author, created = Author.objects.get_or_create(name=input)
        