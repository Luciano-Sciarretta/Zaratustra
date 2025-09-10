from django.db import models
from django.contrib.auth.models import User




class UserInformation(models.Model):
    user  = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE)
    image =   models.ImageField(  blank=True, null=True) 
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_day = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=40, blank=True)
    city    = models.CharField(max_length=40, blank=True)
    adress = models.CharField(max_length=80, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    cell_phone = models.CharField(max_length=30, blank=True)
    document = models.CharField(max_length=30, blank=True)
    cuit = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return self.user.username

