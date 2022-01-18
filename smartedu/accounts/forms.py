from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import date

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Password'
    }))
class DateSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        days = [(day, day) for day in range(1, 32)]
        months = [(month, month) for month in range(1, 13)]
        years = [(year, year) for year in [2018, 2019, 2020]]
        widgets = [
            forms.Select(attrs=attrs, choices=days),
            forms.Select(attrs=attrs, choices=months),
            forms.Select(attrs=attrs, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            year, month, day = value.split('-')
            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(year, month, day)

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

