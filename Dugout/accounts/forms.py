# accounts/forms.py
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="ID")
    password = forms.CharField(label="PW", widget=forms.PasswordInput)