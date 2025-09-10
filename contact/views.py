from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
from contact.models import Query
from contact.forms import QueryForm



class Contact(FormView):
    template_name = "contact/contact.html"
    form_class = QueryForm
    success_url = "send_message"

    def form_valid(self, form):
        form.save()
        form.send_email()
        #Preguntar para que se usa super si este método no es un método de la super clase, sino uno definido por nosotros.
        return super().form_valid(form)
    
class send_message(View):
    template = "contact/send_message.html"
    def get(self, request):
        params = {}
        params["Message"] = "Hi, that's a message"
        return render(request, self.template, params)