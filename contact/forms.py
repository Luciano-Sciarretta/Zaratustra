from django import forms 
from django.forms import ModelForm
from contact.models import Query
# from captcha.fields import CaptchaField

class QueryForm(forms.ModelForm):
    # captcha = CaptchaField()

    class Meta:
        model = Query
        fields = [
            "name",      
            'description',
            'email', 
            'phone',
            
        ]
        labels = {
            "name": 'Ingrese su nombre',
            "email": 'Ingrese su dirección de email',
            "phone": 'Ingrese su número de telefono'
            
        }
    
    def send_email(self,):
        if self.is_valid():
            name =  self.cleaned_data["name"]
            description = self.cleaned_data["description"]
            email = self.cleaned_data["email"]
            phone =  self.cleaned_data["phone"]
        else:
            print("Hubo un error en la validación de datos de l formulario. En contanct/forms/send_email")
        
        #Lógica de envio de mail