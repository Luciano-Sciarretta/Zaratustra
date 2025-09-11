from django.shortcuts import render
from django.views.generic import View
from books.models import Book 
from django.shortcuts import redirect
from books.forms import SearchBookForm
from django.http import HttpResponse
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_protect
from shopping_cart.models import Cart
from shopping_cart.models import CartItem
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

import json
import datetime



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
          print("VAlue de showBook:", value)
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
    
   

# ------------------------------------   clase para mostrar todos los libros  ---------------------


# class OurBooks(View):
#     template = "main_view/our_books.html"
#     books = Book.objects.all()
#     #Agregué el diccionario cart al  controlador del template para mostrar los libros
#     def get(self, request):
#         cart = request.session.get('cart', {})
       
#         request.session['cart'] = cart
#         params = {}
#         books = Book.objects.all()
#         # params["mi_lista"] = [ 1,2, 3, 4, 5, 6]
        
#         params["books"] = books
#         params["cart"] = cart
#         return render(request, self.template, params)
#     def post(self, request):
#         return add_to_cart(request)
  
    
       




#---------------------CART AND LOCAL STORAGE -----------------------------------
# @csrf_protect
# def add_to_cart(request):
#     if request.method == "POST":
#         book_title = request.POST.get("book_title")
#         # print("\n book seleccionado del front:  ", book_title, "\n")
#         book_id = request.POST.get("book_id")
#         book = get_object_or_404(Book, id=book_id)
#         #obtengo o creo  el carro de el usuario.
#         cart, created_cart = Cart.objects.get_or_create(user = request.user)
#         print("cart:" , cart)
      

#  # ----------LÓGICA PARA VER LOS LIBROS DEL CARRITO DEL USUARIO LOGUEADO------------------  
#         user = User.objects.get(username = request.user)
#         cart = Cart.objects.get(user = user)
   
#        # Cambio el stock en la base de datos si el stock es mayor a cero
#         if book.in_stock > 0:
            
#             cart_item, created_cartItem = CartItem.objects.get_or_create(cart= cart, book = book)
#             # print("created de cart_item:  ", book_title,": ",  created_cartItem)

#             cart_item.quantity += 1
#             cart_item.save()
            
#             book.in_stock -= 1
#             book.save()
#             cart_items = CartItem.objects.filter(cart = cart)
            
#             response = {
#                 "status": "success",
#                 "user": request.user.username,
#                 "user_id": request.user.id,
#                 "books": [
#                     {
#                     "book_id": item.book.id,
#                     "book_title": item.book.title,
#                     "quantity": item.quantity,
#                     }
#                     for item in cart_items
#                 ],
#                 "message": f"El libro {book_title} fue agregado correctamente al localStorage"
#             }
           
#         else:
            
#             print(f"No hay stock del libro {book.title}")
#             response = {
#                 "status": "error",
#                 "message": f"No stock available for book: '{book.title}'."
#             }
       
        
#         return JsonResponse(response)
#     else:
#         return JsonResponse({"status": "error", "message": "Invalid request method."})