from django import forms

class SearchBookForm(forms.Form):
    querycom = forms.CharField(label= "",  widget=forms.TextInput(attrs={'class': 'my-search-input', 'placeholder': 'Search by Title, Author or keyword'}))