from django.shortcuts import render
from store.forms import UploadForm 
from books.models import Book
from django.shortcuts import redirect
from django.views.generic import View
from django.http import Http404


def admin_books(request):
    params = {}
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        params['form'] = form
        try:
            if form.is_valid():
                print("valido:  ", form)
                title = form.cleaned_data['title']
                status = form.cleaned_data['status']
                in_stock = form.cleaned_data['in_stock']
                date_of_admision = form.cleaned_data['date_of_admision']
                price = form.cleaned_data['price']
                author = form.cleaned_data['author']
                cover_image = form.cleaned_data['cover_image']
                publication_date = form.cleaned_data['publication_date']
                synopsis = form.cleaned_data['synopsis']
                slug = form.cleaned_data['slug']
                genre = form.cleaned_data['genre']

                new_book = Book(title=title, status=status, in_stock=in_stock, date_of_admision = date_of_admision, price=price, author=author, cover_image=cover_image, publication_date=publication_date, synopsis=synopsis, slug=slug, genre=genre)

                new_book.save()
                return redirect('view_images')
        
            else:
                # El formulario no es válido, renderiza la página nuevamente con el formulario y los errores
                print("Errores del formulario:", form.errors)
                print("NO VALIDO   ")
                return render(request, 'store/form.html', params)
        except Exception as e:
            print("Error al procesar el formulario: ", e)
    else:
        form = UploadForm()
        params["form"] = form
        return render(request, 'store/form.html', params)