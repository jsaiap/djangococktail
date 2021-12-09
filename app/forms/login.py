from django import forms
from django.forms import Form


class LoginForm(Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)