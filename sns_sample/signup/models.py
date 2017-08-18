# coding:utf-8
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class UserInformation()
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email_address'),unique = False)
    first_name = models.CharField(_('first name'),max_length=50,blank=False)
    last_name = models.CharField(_('last name'),max_length=50,blank=False)
    
    
class UserForm(ModelForm):
    class Meta:
        model = CommonUser
        fields = ['username','password','email']
