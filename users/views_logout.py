from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


def logout_page(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logout successful")
        return redirect("login")
    return render(request, "users/logout.html", )