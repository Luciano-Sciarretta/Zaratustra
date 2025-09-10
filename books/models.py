from django.db import models
from django.utils.html import format_html
class Genre(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self,):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self,):
        return self.name
    
class Book(models.Model):
    Stock = "En stock"
    out_of_stock = "Sin stock"
    
    BOOK_APPROVAL = (
        (Stock, "En stock"),
        (out_of_stock, "Sin stock")
        
    )



    status = models.CharField(max_length = 50, choices = BOOK_APPROVAL, default = 'En stock')
    title = models.CharField(max_length = 100)
    date_of_admision = models.DateTimeField("fecha de ingreso")
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  related_name = "libros")
    publication_date = models.DateField("fecha de publicacion")
    cover_image = models.ImageField("imagen de portada", upload_to='book_covers/')
    synopsis = models.TextField()
    slug = models.SlugField(max_length = 200, db_index = True)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    in_stock = models.PositiveIntegerField( default = 1, help_text="Number of available copies of the book.")


    def stock_product(self,):
        if self.status == "En stock":
            return format_html("<span style='color:#2BE6A2;'>{}</span>", self.status)
        elif self.status == "Sin stock":
            return format_html("<span style='color:#E60974;'>{}</span>", self.status)



    def get_absolute_url(self):
        return f"/store/{self.pk}"
    

    def __str__(self,):
        return self.title
    
