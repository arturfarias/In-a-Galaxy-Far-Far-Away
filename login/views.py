from django.shortcuts import  render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login
from .forms import EditPerfilForm

# ===============Formulario de login criado na pagina do index==================
def index(request):
    if  request.user.is_authenticated(): # Redireciona a central caso ja esteja lo
        return redirect(central)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): # verifica se e valido
            login(request, form.get_user())
            return HttpResponseRedirect("/central/")
        else:
            return render(request, "index.html", {"form": form})
    return render(request, "index.html", {"form": AuthenticationForm()})

# ================ Tela central onde fica os menus =============================

def central(request):
     if not request.user.is_authenticated():  # Redireciona ao login caso nao esteja logado
        return redirect(index)
     return render(request,"central.html")

# ================== Tela onde fica as informacoes do usuario ==================
def perfil(request):
     if not request.user.is_authenticated():  # Redireciona ao login caso nao esteja logado
        return redirect(index)
     return render(request,"perfil.html")
# ================== Tela para editar as informacoes do usuario ==================
def editar (request):
    if not request.user.is_authenticated():
        return redirect(index)

    context = {}
    if request.method == 'POST':
        form = EditPerfilForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()

            context['success'] = True
    else:
        form = EditPerfilForm(instance=request.user)
    context['form'] = form

    return render (request,"editar.html",context)
# ================== Tela mudar a senha do usuario ==================
def trocarsenha(request):
    if not request.user.is_authenticated():
        return redirect(index)
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context ['form'] = form

    return render (request,"password.html",context)
