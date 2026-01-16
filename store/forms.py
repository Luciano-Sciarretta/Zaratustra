from django.forms import ModelForm
from books.models import Book, Author
from django import forms

class UploadForm(ModelForm):

    author = forms.CharField(widget=forms.TextInput(), label="Autor")
    
    class Meta:
        model = Book
        fields = ['title', 'stock_quantity',  'price', 'author', 'cover_image', 'synopsis', 'genre']
        


    def clean_author(self):
        author_name = self.cleaned_data['author']
        
        author, created  = Author.objects.get_or_create(name=author_name)
        return author
    
    
    