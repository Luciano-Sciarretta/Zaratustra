from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from users.models import UserInformation
from users.forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages




@login_required
def my_profile(request, user_id):
    
    print("request:", type(request))
    user_info, created = UserInformation.objects.get_or_create(user = request.user)
    print("created:::", created)
    # print("user_info", user_info.cell_phone)
    form = UserEditForm(instance=user_info)
    # print("form", user_info.birth_day)
    print("image:::", user_info.image)
    if request.method == "POST":
        # print("POST",request.POST)
        form = UserEditForm(request.POST, request.FILES or None, instance=user_info)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Your profile has been updated successfully.')
            # print("request.user:::: ", request.user)
            return redirect('profile', user_id=request.user.id) 


    return render(request, "users/profile.html", {"form": form})

# form = UserEditForm(request.POST or None, request.FILES or None, instance=user_info)