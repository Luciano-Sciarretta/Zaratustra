from rest_framework import viewsets
from books.models import Book
from .serializer import ZaratustraRestApiSerializer



class ZaratustraRestApiViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() 
    serializer_class = ZaratustraRestApiSerializer