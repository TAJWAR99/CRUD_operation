from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class UpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']