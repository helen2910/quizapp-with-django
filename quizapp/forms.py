from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded", "placeholder": "First name"}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded", "placeholder": "Last name"}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control rounded", "placeholder": "Username"}), required=True)
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control rounded", "placeholder": "Password"}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control rounded", "placeholder": "Confirm Password"}), required=True)
    
    class Meta:
        model = AppUser
        fields = ["first_name","last_name","username","password1","password2"]