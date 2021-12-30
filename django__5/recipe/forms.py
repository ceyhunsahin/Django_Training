from django import forms
from .models import Student

# class StudentForm(forms.Form) :
#     first_name = forms.CharField(max_length=50, label='your name')
#     last_name = forms.CharField(max_length= 50, label = 'your surname')
#     number = forms.IntegerField(label='your number')


class StudentForm(forms.ModelForm) :
    widget = forms.Textarea(
                                attrs={
                                    'id': 'TA1',
                                    'rows': '10vh',
                                    'cols': '8vw',
                                    'placeholder': 'Enter Your Map Here',
                                    'class': 'textfield-style',
                                    'style': 'max-width: 100%; max-height: 100%;outline: none; border: none; background-color: white; width: 100%; padding: 12px 20px; margin: 8px 0; box-sizing: border-box; font-size: 20px; spellcheck="false";',
                                }
                            )
    first_name = forms.CharField(label= 'Prenom',widget=widget)
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