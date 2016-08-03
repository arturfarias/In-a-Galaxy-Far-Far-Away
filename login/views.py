from django.shortcuts import  render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Perfil # importando as informacoes do banco de dados criado na models
from .forms import CadastroForms # importacao do formulario feito para ser vinculado ao usuario

# ===============Formulario de login criado na pagina do index==================
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): # verifica se e valido
            login(request, form.get_user())
            return HttpResponseRedirect("/central/")
        else:
            return render(request, "index.html", {"form": form,'username':request.user})
    return render(request, "index.html", {"form": AuthenticationForm(),'username':request.user})

# ========== Formulario de registro criado na pagina do registro ===============

def registro(request):
    if not request.user.is_authenticated(): # Redireciona ao login caso nao esteja logado
        return redirect(index)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): # verifica se e valido
            form.save()
            return HttpResponseRedirect("/")
        else: #form2": CadastroForms() esta abaixo apenas para testes, por horas nao remover
            return render(request, "registro.html", {"form": form,"form2": CadastroForms(),'username':request.user})
    return render(request, "registro.html", {"form": UserCreationForm(),"form2": CadastroForms(),'username':request.user })

# ================ Tela central onde fica os menus =============================

def central(request):
     if not request.user.is_authenticated():  # Redireciona ao login caso nao esteja logado
        return redirect(index)
     return render(request,"central.html",{'username':request.user})

# ================== Tela onde fica as informacoes do usuario ==================
def perfil(request):
     if not request.user.is_authenticated():  # Redireciona ao login caso nao esteja logado
        return redirect(index)
     return render(request,"perfil.html",{'username':request.user,
                                          'perfil':request.user.perfil})
