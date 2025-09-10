from django.shortcuts import render
from .forms import CreateUserForm



def user_edit_form(request):
    return render(request, "users/profile.html")