from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib import messages



def login_page(request):
    form = AuthenticationForm(request, request.POST)
    context = {
        'form': form
    }
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('main_page')
    
    return render(request, 'users/login.html', context)