from django import forms

from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["prenom", "last_name", "number"]

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=100, label="Your Name")
#     last_name = forms.CharField(
#         max_length=100, label="Your Surname")
#     number = forms.IntegerField(required=False)