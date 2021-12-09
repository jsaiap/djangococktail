from django import forms
from django.forms import Form


class LoginForm(Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith("univ-amu.fr"):
            self.add_error('email', "*ONLY* univ-amu.fr")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
