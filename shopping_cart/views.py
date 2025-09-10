from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Cart
from .models import CartItem
from django.views import View
from django.views.decorators.csrf import csrf_protect
from books.models import Book
from django.contrib.auth.models import User
from django.http import JsonResponse



def cart(request):
    
    return HttpResponse(f"<h1> Shopping cart de {request.user}</h1>")

class ShowCartUser(View):
    template = 'shopping_cart/shopping_cart.html/'
    def get(self, request):
        try:
            
                user = self.request.user
                cart = Cart.objects.get(user = user)
                cart_books = cart.books.all()
                
                params = {
                    "user": user,
                    "cart": cart,
                    "cart_books": cart_books,
                }
                print('cartbooks::::', cart_books)
                return render(request, self.template, params)
        except Cart.DoesNotExist:
            return HttpResponse(f"<h1> No se encontró el carrito de {user}</h1>")
        



@csrf_protect
def add_to_cart(request):
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        # print("\n book seleccionado del front:  ", book_title, "\n")
        book_id = request.POST.get("book_id")
        book = get_object_or_404(Book, id=book_id)
        #obtengo o creo  el carro de el usuario.
        cart, created_cart = Cart.objects.get_or_create(user = request.user)
        print("cart:" , cart)
      

 # ----------LÓGICA PARA VER LOS LIBROS DEL CARRITO DEL USUARIO LOGUEADO------------------  
        user = User.objects.get(username = request.user)
        cart = Cart.objects.get(user = user)
   
       # Cambio el stock en la base de datos si el stock es mayor a cero
        if book.in_stock > 0:
            
            cart_item, created_cartItem = CartItem.objects.get_or_create(cart= cart, book = book)
            # print("created de cart_item:  ", book_title,": ",  created_cartItem)

            cart_item.quantity += 1
            cart_item.save()
            
            book.in_stock -= 1
            book.save()
            cart_items = CartItem.objects.filter(cart = cart)
            
            response = {
                "status": "success",
                "user": request.user.username,
                "user_id": request.user.id,
                "books": [
                    {
                    "book_id": item.book.id,
                    "book_title": item.book.title,
                    "quantity": item.quantity,
                    }
                    for item in cart_items
                ],
                "message": f"El libro {book_title} fue agregado correctamente al localStorage"
            }
           
        else:
            
            print(f"No hay stock del libro {book.title}")
            response = {
                "status": "error",
                "message": f"No stock available for book: '{book.title}'."
            }
       
        
        return JsonResponse(response)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."})
    

@csrf_protect
def remove_from_cart(request, pk):
    if request.method == "POST":
        
        cart = get_object_or_404(Cart, user = request.user)
        cart_item = get_object_or_404(CartItem, book_id=pk, cart=cart)
        cart_item.delete()

        # cart_items = CartItem.objects.filter(cart = cart)
        # print("cart items:    ", cart_items)


        response = {
            "status": "success",
            "message": f"El libro con id {pk} fue eliminado del carrito"
        }
        return JsonResponse(response)

    else:
         return JsonResponse({"status": "error", "message": "Invalid request method."})