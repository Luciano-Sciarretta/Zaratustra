from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserInformation

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(forms.ModelForm): 
    class Meta:
        model = UserInformation
        fields =["user", "image", "name", "last_name", "birth_day", "country", "state", "city", "adress", "postal_code", "phone", "cell_phone", "document", "cuit"]