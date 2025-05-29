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
    
    def clean_beds(self):
        beds = self.cleaned_data.get('number_of_beds')
        if beds < 1:
            raise forms.ValidationError("Deve haver pelo menos 1 leito")
        return beds