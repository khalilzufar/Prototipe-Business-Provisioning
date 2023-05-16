from django import forms
from .models import Myuser

class UserForm(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = ['name', 'email', 'age']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }
