 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
 
IDENTITY=[('Student'), ('NYUSH Student'), ('NYUSH Faculty')]

class FormUserRegistration (UserCreationForm):
    email=forms.EmailField(required=True)
    # status=forms.Select(choices=IDENTITY)
    class Meta:
        model=User
        fields= ['username', 'email', 'password1', 'password2']
        