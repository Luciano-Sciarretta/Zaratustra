from django.shortcuts import render
from django.views.generic import View
from books.models import Book 
from books.forms import SearchBookForm
from django.http import HttpResponse, JsonResponse
import json




def about_us(request):
    context = {}
    return render(request, "main_view/about_us.html", context)



 # ----------------   barra de búsqueda  ---------------------------
def index(request):
    context = {   
    }
    books = Book.objects.all()
    context["books"] = books
    search = SearchBookForm()
    context["search"] = search
    return render(request, "main_view/main_view.html", context)

#Barra de búsqueda
class SearchBook(View): 
    def get(self, request):
       
       try:
           input_word = request.GET.get("q", "")   
           print("input-word:", input_word) 
           books = Book.objects.filter(title__icontains = input_word)
           print("Books:",  books)
           result = []
           for book in books:
               data={}
               data["title"] = book.title
               result.append(data)
             
       except Exception as e:
           return JsonResponse({"error": str(e)}, status=500)
       
       return JsonResponse(result, safe=False)  
    
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
    
   




