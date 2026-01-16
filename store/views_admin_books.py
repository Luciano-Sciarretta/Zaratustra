from django.urls import reverse_lazy
from store.forms import UploadForm 
from books.models import Book, Author
from django.contrib import messages
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    form_class = UploadForm
    template_name = 'store/form.html'
    success_url = reverse_lazy('all_books')
    
    def  form_valid(self, form):
        book = form.save()
        messages.success(self.request, f"Book '{book.title}' was created successfully.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "A problem has occurred,  please check the form")
        print("Errores en el formulario:", form.errors )
        return  super().form_invalid(form)
    
    
        
    
def api_authors_search(request):
    search_query = request.GET.get("q")
    # print("Search query", search_query)
    authors_list = []
    
    
    if len(str(search_query)) >= 3:
        queryset = Author.objects.filter(name__icontains = search_query)
        authors_list = list(queryset.values('id', 'name'))
        # print('authors:', authors_list)
        data = {
        "success": True,
        "authors": authors_list,
        "message": f"Encontrados {len(authors_list)} autores" if authors_list else "No se encontraron autores"
        
    }
    else:
        data = {
            'success': False,
            "authors": [],
             "message": "Ingrese al menos 3 caracteres para buscar"
        }
        
    
    return JsonResponse(data)
    










    
# def admin_books(request):
#     params = {}
#     if request.method == "POST":
#         form = UploadForm(request.POST, request.FILES)
#         params['form'] = form
#         try:
            
#             if form.is_valid():
#                 new_book = form.save()
#                 messages.success(request, "Libro creado exitosamente!")
#                 return redirect('books')
        
#             else:
#                 print("Errores del formulario:", form.errors)
#                 messages.error(request, "Error al procesar el formulario")
#                 return render(request, 'store/form.html')
            
#         except Exception as e:
#             print("Error al procesar el formulario: ", e)
#             messages.error(request, f"Ocurrió un problema.Error: {e}")
#             return render(request, 'store/form.html')
#     else:
#         form = UploadForm()
#         params["form"] = form
#         return render(request, 'store/form.html', params)