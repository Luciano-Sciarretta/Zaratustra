
from django.urls import path
from users import views_login
from users import views_logout
from users import views_register
from users import views_profile








urlpatterns = [
   
    
    path("login", views_login.login_page, name="login"),
    path("logout", views_logout.logout_page, name="logout"),
    path("register", views_register.register_page, name="register"),
    
    path("profile/<int:user_id>/", views_profile.my_profile, name="profile")
]
