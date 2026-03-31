

    
def cart_count(request):
     from shopping_cart.models import Cart
     count = 0
     if request.user.is_authenticated:
         cart = Cart.objects.filter(user = request.user).first()
         if cart:
             cart_items = cart.cartitem_set.all()
             for item in cart_items:
                 count += item.quantity
             
         return {'cart_count': count}
     return {'cart_count' : 0}
