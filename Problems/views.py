from django.shortcuts import render,redirect,get_object_or_404
from .forms import CadastroItens,ListaProblema,EditarProblema
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

def list_detail(request, pk):
    post = get_object_or_404(Problema, pk=pk)
    return render(request, 'list_detail.html', {'post': post})

def list_edit(request, pk):
    post = get_object_or_404(Problema, pk=pk)
    if request.method == "POST":
        form = EditarProblema(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('list_detail', pk=post.pk)
    else:
        form = EditarProblema(instance=post)
    return render(request, 'list_edit.html', {'form': form})
