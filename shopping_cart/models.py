from django.db import models
from books.models import Book
from django.contrib.auth.models import User





class Cart(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    books = models.ManyToManyField(Book, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f"{self.quantity} of book: {self.book.title} in cart of {self.cart.user.username}"