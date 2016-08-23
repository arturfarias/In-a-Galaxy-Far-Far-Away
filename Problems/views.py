from django.shortcuts import render,redirect
from .forms import CadastroItens,ListaProblema
from .models import Problema

def cadastro_itens(request):
     if not request.user.is_authenticated():
         return redirect(index)

     context = {}
     if request.method == 'POST':
         form = CadastroItens(request.POST)
         if form.is_valid():
             form.save()
             context['success'] = True
     else:
         form = CadastroItens()
     context['form'] = form

     return render (request,"itens.html",context)

def problemas(request):
     if not request.user.is_authenticated():
         return redirect(index)
     context = {}
     if request.method == 'POST':
         form = ListaProblema(request.POST)
         if form.is_valid():
             form.save()
             context['success'] = True
     else:
         form = ListaProblema()
     context['form'] = form

     return render (request,"problemas.html",context)

def lista(request):
     if not request.user.is_authenticated():
         return redirect(index)

     variavel = Problema.objects.all()

     return render(request,"lista.html",{'objetos':variavel})
