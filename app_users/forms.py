from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

"""used to add email and first_name fields at Django UserCreationForm"""


class PersonalUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Votre nom d\'utilisateur'}
            ),
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Votre Prénom'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Votre adresse email'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PersonalUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
