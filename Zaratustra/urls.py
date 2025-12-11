
from django.contrib import admin
from django.urls import path
from django.http import HttpRequest
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from store.sitemaps import StoreSitemaps, SingleBookSitemaps
from main_view.sitemaps import MainViewSitemaps


sitemaps = {
    "store_all_books": StoreSitemaps,
    "store_single_books": SingleBookSitemaps,
    "main_view": MainViewSitemaps
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path("books/", include("books.urls")),
    path("store/", include('store.urls')),
    path("users/", include("users.urls")),
    path("shopping_cart/", include('shopping_cart.urls')),
    path("", include("main_view.urls")),
    path("api/", include("api.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name = "django.contrib.sitemaps.views.sitemap")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

