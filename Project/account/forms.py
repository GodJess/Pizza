from django.forms import ModelForm, TextInput, Textarea
from .models import User


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'mail']

        widgets={
            'login': TextInput(attrs={
                "name": "login",
                "placeholder": "Введите логин",
            }),
            'password': TextInput(attrs={
                'type': 'password',
                "name": "password",
                "placeholder": "Введите пароль",
            }),
            'mail': TextInput(attrs={
                "name": "mail",
                "placeholder": "Введите mail",
            })
        }