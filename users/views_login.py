from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages


def login_page(request):
    params = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            return redirect("main_page")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return render(request, "users/login.html")
        
    return render(request, "users/login.html", params)
