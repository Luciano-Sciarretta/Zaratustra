from django.shortcuts import render
from .forms import CreateUserForm
from django.shortcuts import redirect


def register_page(request):
    params = {}
    form = CreateUserForm()
    params["form"] = form

    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Guarda usuario")
                return redirect("login")
            except:
                print("No Funca")
                
            
        else:
            
            return redirect("register")
        
    return render(request, "users/register.html", params)

