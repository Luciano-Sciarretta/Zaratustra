from django.contrib import admin
from books.models import Book
from books.models import Genre
from books.models import Author
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class GenreAdmin(admin.ModelAdmin):
    inlines = [BookInline]

class LibroAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relacion", {"fields":  ["author", "genre"] }  ),
        ("Datos Generales", {"fields": ["title", "status", "in_stock", "date_of_admision", "price", "publication_date", "cover_image", "synopsis", "slug"]
        })
    ]

    list_display = ["title", "author", "genre" ,"stock_product", "date_of_admision", "price", "in_stock", "upper_case_name"]
    ordering = ["-date_of_admision"]
    list_filter = ["title", "publication_date", "price"]
    search_fields = [ "title", "status",  "genre__name", "author__name"]
    actions = ['change_status', "export_to_json", "view_books"]


    @admin.display(description = "Name")
    def upper_case_name(self, obj):
        return ("%s  %s" % (obj.title, obj.status)).upper()
    
    def change_status(self, request, queryset):
        count = queryset.count()
        for book in queryset:
            print("Estado actual del libro:", book.status)
            if book.status == "En stock":
                book.status = "Sin stock"
            else:
                book.status = "En stock"
            
            
            book.save()

        
        message = "Se han actualizado %s registros exitosamente" % count

        self.message_user(request, " %s " % message ) 
    change_status.short_description = "Change Status"

    def export_to_json(self, request, queryset):
        response = HttpResponse(content_type = "application/json")
        #Un serializer es una clase que define cómo se deben serializar (es decir, convertir en un formato legible y portable) los objetos complejos en Django, como modelos de base de datos o consultas de queryset, en formatos de datos como JSON, XML o YAML.
        serializers.serialize("json", queryset, stream = response)
        return response

    def view_books(self, request, queryset):
        params = {}
        books = Book.objects.all()
        params["books"] = books
        return render(request, "admin/books/books.html", params)
    view_books.short_description = "View Books"

admin.site.register(Book, LibroAdmin)
admin.site.register(Author)
admin.site.register(Genre, GenreAdmin)

