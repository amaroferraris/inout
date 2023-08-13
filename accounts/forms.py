from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InForm(ModelForm):
    class Meta:
        model = In
        fields = ['amount', 'description', 'category', 'user_in']


class OutForm(ModelForm):
    class Meta:
        model = Out
        fields = ['amount', 'description', 'category']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
