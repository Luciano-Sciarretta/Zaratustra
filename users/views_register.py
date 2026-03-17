from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages


def register_page(request):
    params = {}
    form = UserCreationForm(request.POST or None)
    params["form"] = form

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration complete! You are now logged in.')
    
            if user is not None:
                login(request, user)
                return redirect("main_page")
            else:
                return redirect('login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below")
    return render(request, "users/register.html", params)

