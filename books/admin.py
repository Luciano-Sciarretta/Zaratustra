from django.contrib import admin
from books.models import Book
from books.models import Genre
from books.models import Author
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render



admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)

