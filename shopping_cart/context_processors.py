from shopping_cart.models import CartItem, Cart

    
def cart_count(request):
     if request.user.is_authenticated:
         cart = Cart.objects.filter(user = request.user)
         if cart:
             count = cart.books.count()
             
