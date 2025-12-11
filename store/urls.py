from django.urls import path
from store.views import AllBooks
from store.views import SingleBook
from store import views_admin_books

urlpatterns = [

    path("admin_books/", views_admin_books.BookCreateView.as_view(), name = "admin_books"),
    path("", AllBooks.as_view(), name="all_books"),
    path("<str:pk>/", SingleBook.as_view(), name="single_book")
   
]
