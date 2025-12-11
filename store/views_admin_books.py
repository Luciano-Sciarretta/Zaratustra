from django.shortcuts import render
from django.urls import reverse_lazy
from store.forms import UploadForm 
from books.models import Book
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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