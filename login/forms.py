# coding: utf-8
from django import forms
from django.contrib.auth.models import User

# Formulario para editar gerar um form para editar as opçoes de usuario
class EditPerfilForm(forms.ModelForm):

#função para comparar se o email modificado ja esta em uso
    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('E-mail ja cadastrado')
        return email

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
