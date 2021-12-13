from django import forms
from django.forms import Form


class LoginForm(Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)

    # def clean_email(self):
    # username = self.cleaned_data['username']
    # if not username.endswith("univ-amu.fr"):
    #   self.add_error('email', "*ONLY* univ-amu.fr")
    # return username

    # def clean_password(self):
    #    password = self.cleaned_data['password']
