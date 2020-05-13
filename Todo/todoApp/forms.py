from django import forms
from todoApp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
