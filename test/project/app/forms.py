from django import forms
from .models import sample

class MyForm(forms.ModelForm):
    class Meta:
        model=sample
        fields='__all__'