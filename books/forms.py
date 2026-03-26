from django import forms

class SearchBookForm(forms.Form):
    querycom = forms.CharField(label= "",  widget=forms.TextInput(attrs={ 'placeholder': 'Search by Title, Author or keyword'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'my-search-input'})
            # print("querycom:", field.widget.attrs['class'])
                