from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import UserInformation
from django.db.models import signals

@receiver(post_save, sender=User)
def create_user_information(sender, instance, created, **kwargs):

      if created: 
        UserInformation.objects.create(user=instance)
        

@receiver(post_save, sender=UserInformation)
def update_user_information(sender, instance, created, **kwargs):
    if created:
        print(f"Se a creado la información del usuario: {instance.user}")
    else:
        print(f"Se ha modificado la información del usuario: {instance.user}")
# sender: El remitente de la señal, en este caso, será la clase User.
# instance: La instancia del objeto User que se acaba de guardar.
# created: Un booleano que indica si el objeto User acaba de ser creado o actualizado.