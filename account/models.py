from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField("Email", max_length=255, unique=True)
    username = models.CharField("Username", max_length=35, unique=True, null=True, blank=True)
    last_login = None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


"""
AbstractBaseUser basically provide only 3 fields id, password and last_login, So i am using this one
AbstractUser provide 11 all fields and you can add extra fields 
"""


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True, default='')
    phone = models.CharField("Phone", max_length=20,null=True, blank=True, default='')
    first_name = models.CharField('First Name', max_length=255, null=True, blank=True, default='')
    last_name = models.CharField('Last Name', max_length=255, null=True, blank=True, default='')
