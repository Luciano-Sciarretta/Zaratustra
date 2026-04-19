from django.shortcuts import render, redirect
from django.views.generic import View
from books.models import Book 
from books.forms import SearchBookForm
from django.http import HttpResponse, JsonResponse
import json
from django.db.models import Q




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
           books = Book.objects.filter(Q(title__icontains=input_word) | Q(author__name__icontains = input_word)).distinct()
           result = []
           for book in books:
               data={}
               data["title"] =book.title
               data["id"]= book.id
               data['slug'] = book.slug
               data['author'] = book.author.name
               result.append(data)
        #    print(".\ndata:", data, ".\n")  
       except Exception as e:
           return JsonResponse({"error": str(e)}, status=500)
       
       return JsonResponse(result, safe=False)  
    
class ShowBook(View):
   
   def get(self, request):
       querycom = request.GET.get('querycom', "").strip()
       
       
       if querycom:
        book = Book.objects.filter(Q(title__icontains=querycom) | Q(author__name__icontains = querycom)).distinct().first()
        if book:
            return redirect('single_book', slug=book.slug)
       return redirect('main_page')
    
    
   




