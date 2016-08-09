# coding: utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CadastroForms(UserCreationForm):
    # Criando o camp do form do email
    email = forms.EmailField(label='E-mail')
    # Incluindo o form de email ao cadastro
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email
        # salvando o form de email
    def save(self,commit=True):
        user = super(CadastroForms,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit :
            user.save()
        return user
