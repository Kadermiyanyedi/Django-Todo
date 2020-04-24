from django import forms
from todoApp.models import *


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
