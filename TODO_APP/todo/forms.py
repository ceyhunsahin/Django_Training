from django import forms
from .models import Todo

class TodoAddForm(forms.ModelForm) :
    class Meta :
        model = Todo
        fields = ['title']
        # ordering = ['-create_date'] bunlar normal modelden import edilirken kullanilir
        # verbose_name = 'pizza'

class TodoUpdateForm(forms.ModelForm):
    class Meta :
        model = Todo
        fields = ['title', 'completed']
