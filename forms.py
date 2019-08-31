from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TodoForm(forms.Form):
    text = forms.CharField(max_length=50,
                           widget = forms.TextInput(attrs = {'placeholder': 'Add a todo e.g. Buy groceries',
                                                             'class': 'form-control'}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First name of contact'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last name of contact'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email','placeholder': ('E-mail address')}))
