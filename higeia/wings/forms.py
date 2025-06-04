# forms.py
from django import forms
from .models import Wing

class WingForm(forms.ModelForm):
    class Meta:
        model = Wing
        fields = ['code', 'name', 'number_of_beds']
        labels = {
            'code': 'Código',
            'name': 'Nome',
            'number_of_beds': 'Número de leitos',
        }
