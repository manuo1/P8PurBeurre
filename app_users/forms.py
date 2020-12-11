
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

"""used to add email field at Django UserCreationForm"""
class PersonalUserCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'first_name', 'email', 'password1', 'password2']
