from django.shortcuts import  render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Perfil # importando as informações do banco de dados criado na models


"""
Falta  mudar texto para portugues
"""
# ===============Formulário de login criado na pagina do index==================
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): # verifica se é valido
            login(request, form.get_user())
            return HttpResponseRedirect("/central/")
        else:
            return render(request, "index.html", {"form": form})
    return render(request, "index.html", {"form": AuthenticationForm()})

"""
Falta mudar texto que aparece para portugues,
"""

# ========== Formulário de registro criado na pagina do registro ===============

def registro(request):
    if not request.user.is_authenticated(): # Redireciona ao login caso não esteja logado
        return redirect(index)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): # verifica se é valido
            form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "registro.html", {"form": form})
    return render(request, "registro.html", {"form": UserCreationForm() })

# ================ Tela central onde fica os menus =============================
def central(request):
     if not request.user.is_authenticated():  # Redireciona ao login caso não esteja logado
        return redirect(index)
     return render(request,"central.html")
# ================== Tela onde fica as informações do usuario ==================
def perfil(request):
     if not request.user.is_authenticated():  # Redireciona ao login caso não esteja logado
        return redirect(index)
     return render(request,"perfil.html",{'username':request.user,
                                          'perfil':request.user.perfil})
