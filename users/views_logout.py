from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout


def logout_page(request):
    logout(request)
    print("sesion terminada")
    redirect("login")
    return render(request, "users/logout.html", )