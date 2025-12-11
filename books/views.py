from django.shortcuts import render

#---------------------------------------
def index_books(request):
 
    return  render(request, "books/books.html")
