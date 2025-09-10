from django.forms import ModelForm
from .models import Book
from django import forms

class SearchBookForm(forms.Form):
    querycom = forms.CharField(label= "",  widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control', 'placeholder': 'Search by Title, Author or keyword','style': 'text-align: center;' }))