from django.urls import path
from .views import ShowCartUser
from .views import remove_from_cart


urlpatterns = [

path("", ShowCartUser.as_view(), name="shopping_cart"),
path("remove_from_cart/<int:pk>/", remove_from_cart, name="remove_from_cart")

]