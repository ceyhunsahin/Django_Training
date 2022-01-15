
from pages.models import ContactFormMod
from django import forms

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'FirstName'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'LastName'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Your Email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs= {
        'class' : 'form-control', 'placeholder' : 'Your Phone'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs= {
        'class' : 'form-control', 'placeholder' : 'Message'
    }))


    class Meta:
        model = ContactFormMod
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']