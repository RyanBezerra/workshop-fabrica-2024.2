from django import forms
from .models import Menu
from .utils import get_localidades  # Importando a função corretamente

class MenuForm(forms.ModelForm):
    localidade = forms.ChoiceField(choices=get_localidades(), required=False)

    class Meta:
        model = Menu
        fields = ['nome', 'idade', 'sexo', 'localidade']

