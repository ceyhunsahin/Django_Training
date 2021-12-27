from django import forms
from .models import Student

# class StudentForm(forms.Form) :
#     first_name = forms.CharField(max_length=50, label='your name')
#     last_name = forms.CharField(max_length= 50, label = 'your surname')
#     number = forms.IntegerField(label='your number')


class StudentForm(forms.ModelForm) :
    first_name = forms.CharField(label= 'Prenom')
    class Meta:
        model = Student
        # fields = ('first_name', 'last_name', 'number')
        fields = '__all__'

    # def __init__(self):
    #     super(StudentForm, self).__init__()
    #     self.fields['last_name'].label = 'Nom'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['last_name'].label = 'Nom'