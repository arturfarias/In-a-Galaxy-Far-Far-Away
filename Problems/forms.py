from django import forms
from .models import Equipamento,Problema

class CadastroItens(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['laboratorio','numero_de_Serie','tipo_de_Equipamento']

class ListaProblema(forms.ModelForm):
    class Meta:
        model = Problema
        fields = ['equipamento','descricao']
