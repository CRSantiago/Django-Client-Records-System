from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    def clean_email(self):
        submitted_data = self.cleaned_data['email']
        if '@companyname.com' not in submitted_data:
            raise forms.ValidationError('You must register using a Company address')
        return submitted_data

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]