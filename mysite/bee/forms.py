from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserRegister(UserCreationForm):
	username = forms.CharField(label = 'Логин', widget = forms.TextInput(attrs = {'class': ''}))
	password1 = forms.CharField(label = 'Пароль')
	password2 = forms.CharField(label = 'Повтор пароля')
	email = forms.EmailField(label = 'Email')

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email')

class UserAuthentication(AuthenticationForm):
	username = forms.CharField(label = 'Логин', widget = forms.TextInput(attrs = {'class': 'input100'}))
	password = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs = {'class': 'input100'}))


class PromoCode(forms.Form):
	text = forms.CharField(max_length = 255, label = 'Промо код')