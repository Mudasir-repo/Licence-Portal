from django.db import models
from django.forms import fields
from django import forms
from .models import Licence_Data
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model= User
        fields = ['username', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwod do not match!")
        return cleaned_data

class LicenceForm(forms.ModelForm):
    class Meta:
        model = Licence_Data
        fields = ['name','image','pdf']