from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'ID:',
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'PW:',
        })

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'ID:',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'PW:',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'PW 확인:',
        })
