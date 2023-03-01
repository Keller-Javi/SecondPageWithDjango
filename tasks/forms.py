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
