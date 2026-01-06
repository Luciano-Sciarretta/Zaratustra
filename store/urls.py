from django.urls import path
from store.views import AllBooks
from store.views import SingleBook 
from store import views_admin_books

urlpatterns = [

    path("admin_books/", views_admin_books.BookCreateView.as_view(), name = "admin_books"),
    path("", AllBooks.as_view(), name="all_books"),
    path("api/authors/search/",views_admin_books.api_authors_search, name= 'api_authors_search'),
    path("<str:pk>/", SingleBook.as_view(), name="single_book"),
]
