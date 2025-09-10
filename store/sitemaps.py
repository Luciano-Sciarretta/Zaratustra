from django.contrib import sitemaps
from django.urls import reverse
from books.models import Book

class StoreSitemaps(sitemaps.Sitemap):
    priority = 0.7
    changefreq = "daily"
    
    def items(self):
        return ["all_books"]
    
    def location(self, item):
        return reverse(item)
    
class SingleBookSitemaps(sitemaps.Sitemap):
    priority = 0.8
    changefreq = "daily"
    
    
    def items(self):
        return Book.objects.all()

    def location(self, item):
        return item.get_absolute_url()