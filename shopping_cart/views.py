from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Cart
from .models import CartItem
from django.views import View
from django.views.decorators.csrf import csrf_protect
from books.models import Book
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class ShowCartUser(LoginRequiredMixin,View):
    template = 'shopping_cart/shopping_cart.html/'
    def get(self, request):
        
      user = self.request.user
      cart = Cart.objects.filter(user = user).first()
      cart_items = cart.cartitem_set.all() if cart else []
      
      params = {
          
          "cart": cart,
          "cart_items": cart_items,
      }
      return render(request, self.template, params)
  
        



@csrf_protect
def add_to_cart(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = get_object_or_404(Book, id=book_id)
        
        cart, created_cart = Cart.objects.get_or_create(user = request.user)
    
        if book.is_available:
            cart_item, created = CartItem.objects.get_or_create(cart= cart, book = book)
            cart_item.add_to_cart()
            
            book.stock_quantity -= 1
            book.save()
            messages.success(request, f'{book.title} agregado al carrito de compras.')
            return redirect('all_books')
            
        else:
          messages.error(request, "The book isn't available")
          return redirect('all_books')
 

@csrf_protect
def remove_from_cart(request, pk):
    if request.method == "POST":
        cart = get_object_or_404(Cart, user = request.user)
        cart_item = get_object_or_404(CartItem, book_id=pk, cart=cart)
        
        title = cart_item.book.title
        author = cart_item.book.author
        
        cart_item.book.stock_quantity += 1
        cart_item.book.save()
        
        cart_item.remove_unit()
        
        messages.success(request, f'El libro {title} del autor {author} fué borrado exitosamente!')

        return redirect('shopping_cart')
      

    