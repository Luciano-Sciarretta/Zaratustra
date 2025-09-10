from django.urls import path
from contact import views
from contact.views import Contact
from contact.views import send_message

urlpatterns = [
    #Vistas basadas en clases que estan en el views.py
    path("", Contact.as_view(), name = "contact"),
    path("send_message", send_message.as_view(), name="send_message")
]
