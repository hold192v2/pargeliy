from django import forms
from  django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Введите Логин:", widget=forms.TextInput(attrs={"autofocus": True,
                                                             "class": "form-control item form-group",
                                                             "placeholder":"Логин"}))
    password = forms.CharField(label="Введите Пароль:", widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                             "class": 'form-control item form-group',
                                                             "placeholder": "Пароль"}))
    class Meta:
        model = User
        fields = ('username', 'password')
