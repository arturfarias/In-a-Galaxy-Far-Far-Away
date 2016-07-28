from django.shortcuts import  render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Perfil


"""
Falta  mudar texto para portugues
"""
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect("/central/")
        else:
            return render(request, "index.html", {"form": form})
    return render(request, "index.html", {"form": AuthenticationForm()})

"""
Falta mudar texto que aparece para portugues,
"""
def registro(request):
    if not request.user.is_authenticated():
        return redirect(index)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "registro.html", {"form": form})
    return render(request, "registro.html", {"form": UserCreationForm() })

def central(request):
     if not request.user.is_authenticated():
        return redirect(index)
     return render(request,"central.html")

def perfil(request):
     if not request.user.is_authenticated():
        return redirect(index)
     return render(request,"perfil.html",{'username':request.user,
                                          'perfil':request.user.perfil})
