from django.shortcuts import render

#---------------------------------------
def index_books(request):
    context = {
        'nombre': 'libros', 
        'genero': 'terror'
    }
    return  render(request, "books/books.html", context)
