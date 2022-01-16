from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Password'
    }))
class RegisterForm(UserCreationForm) :

    first_name = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'FirstName'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'LastName'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'UserName'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Your Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Password Confirmation'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

