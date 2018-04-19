from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label=_('Enter Username'), min_length=4, max_length=30)
    email = forms.EmailField(label=_('Enter email address'), max_length=30)
    password1 = forms.CharField(label=_('Enter password here'), widget=forms.PasswordInput, min_length=8, max_length=30)
    password2 = forms.CharField(label=_('Confirm password'), widget=forms.PasswordInput, max_length=30)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError(_("Username already exists"))
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError(_("Email already exists"))
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Password don't match"))

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
