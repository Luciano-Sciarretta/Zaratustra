from django.shortcuts import render
from django.views.generic import View
from books.models import Book 
from books.forms import SearchBookForm
from django.http import HttpResponse
import json




def about_us(request):
    context = {}
    return render(request, "main_view/about_us.html", context)

# Mostrar todos los libros y lógica de carrito

 # ----------------   barra de búsqueda  ---------------------------
def index(request):
    context = {
        "nombre": "Luciano",
        "proyecto": 'zaratustra'
    }
    books = Book.objects.all()
    context["books"] = books
    search = SearchBookForm()
    context["search"] = search
    return render(request, "main_view/main_view.html", context)

#Barra de búsqueda
class SearchBook(View): 
    def get(self, request):
       
       if request.headers.get('x-requested-with') == 'XMLHttpRequest':
           
           input_word = request.GET.get("term", "")    
           
           books = Book.objects.filter(title__icontains = input_word)
           result = []
           for book in books:
               data={}
               data["label"] = book.title
               result.append(data)
           data_json= json.dumps(result)   
       else:
           data_json="Error in search bar"
       mimetype ="application/json"  
       return HttpResponse(data_json, mimetype)  
    
class ShowBook(View):
   
    def get(self, request):
      if request.headers.get('x-requested-with') == 'XMLHttpRequest':
         
          try:
            value = request.GET['value']
           
          except:
              print("No esta value")  
        #   print("VAlue de showBook:", value)
          book = Book.objects.filter(title__icontains = value)
          result = [] 
          for attr in book:
              print("Print de ajax-search-bar",  attr.title)
              print("Print de ajax-search-bar",  attr.status)
              print("Print de ajax-search-bar",  attr.cover_image)

              data = {}              
              data["title"] = attr.title
              data["status"] = attr.status
              data["cover_image"] = attr.cover_image.url
              result.append(data)
          data_json = json.dumps(result)
      else:
          data_json = "No funca"   
      mimetype = "application/json"
      return HttpResponse(data_json, mimetype)
    
   




