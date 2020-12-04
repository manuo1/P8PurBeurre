
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

"""used to add email field at Django UserCreationForm"""
class PersonalUserCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
