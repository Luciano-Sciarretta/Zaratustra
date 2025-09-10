from django.forms import ModelForm
from books.models import Book

class UploadForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'status', "in_stock", 'date_of_admision', 'price', 'author', 'publication_date', 'cover_image', 'synopsis', 'slug', 'genre']

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)