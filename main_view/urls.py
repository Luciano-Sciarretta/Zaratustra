
from django.contrib import admin
from django.urls import path
# from .views import OurBooks
from .views import SearchBook
from .views import ShowBook
from . import views


urlpatterns = [
    
    path('', views.index, name="main_page"),
    path('about_us/', views.about_us, name="about_us"),
    # path("our_books/", OurBooks.as_view(), name="our_books"),
    path("search_books/", SearchBook.as_view(), name="search_books"),
    path("show_book/", ShowBook.as_view(), name="show_book"),
    
    
    
]
