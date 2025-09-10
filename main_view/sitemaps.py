from django.contrib import sitemaps
from django.urls import reverse


class MainViewSitemaps(sitemaps.Sitemap):
    priority = 0.9
    changefreq = "daily"
    
    def items(self):
        return ["main_page"]
    
    def location(self, item):
        return reverse(item)