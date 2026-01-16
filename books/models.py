from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self,):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self,):
        return self.name
    
class Book(models.Model):

    title = models.CharField(max_length = 100)
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  related_name = "libros")
    cover_image = models.ImageField("imagen de portada", upload_to='book_covers/', default='book_covers/CoverNotAvailable.jpg' ,blank=True)
    synopsis = models.TextField()
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    stock_quantity = models.IntegerField(default=1, verbose_name="Stock Quantity")
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True, editable=False )
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def is_available(self, ):
        return self.stock_quantity > 0


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            final_slug = base_slug
            counter = 1

            while Book.objects.filter(slug= final_slug).exists():
                final_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = final_slug

        super().save(*args, **kwargs)

    #Método para el admin panel
    
    # def available_admin(self):
    #     if self.stock_quantity:
    #         return format_html("<span style='color: green;'>{}</span>", self.stock_quantity)
    #     else:
    #         return format_html("<span style='color:red;'>{}</span>", 0)


    def get_absolute_url(self):
        return f"/store/{self.pk}"
    

    def __str__(self,):
        return self.title
    
