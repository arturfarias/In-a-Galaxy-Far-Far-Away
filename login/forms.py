from django import forms
from .models import Perfil

class CadastroForms(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('nome', 'sobrenome','sexo', 'datanascimento','email',
                   'telefone','senha', 'endereco','numero', 'complemento',
                   'cep', 'bairro','estado', 'cidade','foto',)
