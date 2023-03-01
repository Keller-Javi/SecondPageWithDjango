from turtle import textinput
from django import forms
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write title of this task'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write description of this task'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        } 
    # Es un formulario basado en el modelo Task, que pide al usuario lo que se indica en fields


class FilterTask(forms.Form):
    options = [(1, 'None'), (2, 'Importants'), (3, 'Not importants'),
               (4, 'Completed'), (5, 'Not completed')]
    filter_option = forms.ChoiceField(widget=forms.RadioSelect, choices=options)
    
    widgets = forms.SelectDateWidget(attrs={'class': 'custom-select', 'id': 'inputGroupSelect03'})
