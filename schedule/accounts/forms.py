from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

class LogInForm(AuthenticationForm, LoginRequiredMixin):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        

