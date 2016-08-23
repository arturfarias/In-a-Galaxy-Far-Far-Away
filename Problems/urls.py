from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^central/itens/$', views.cadastro_itens,name = "itens"), #tela de mudar senha
    url(r'^central/problemas/$', views.problemas,name = "problemas"), #tela de mudar senha
    url(r'^central/lista/$', views.lista,name = "lista"), #tela de mudar senha
]
