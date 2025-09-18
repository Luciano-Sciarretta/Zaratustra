from django.shortcuts import render
from books.models import Book
from django.views.generic import View
from shopping_cart.views import add_to_cart
from django.http import Http404




class AllBooks(View):
    template = "store/all_books.html"
    books = Book.objects.all()
    #Agregué el diccionario cart al  controlador del template para mostrar los libros
    def get(self, request):
        cart = request.session.get('cart', {})
       
        request.session['cart'] = cart
        params = {}
        books = Book.objects.all()
        
        params["books"] = books
        params["cart"] = cart
        return render(request, self.template, params)
    def post(self, request):
        return add_to_cart(request)
  



class SingleBook(View): 
    template = "store/single_book.html"
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            print("book", book)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        context = {
            "title": book.title,
            "description": book.synopsis,
            "image": book.cover_image,
            "author": book.author,
            "price": book.price
        }

        return  render( request, self.template, context )

















