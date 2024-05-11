from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()