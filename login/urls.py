from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.index,name = "index"),#Pagina index onde se localiza o login
    url(r'central/$', views.central), #Pagina central do aplicativo
    url(r'^central/perfil/$', views.perfil,name = "perfil"), #Pagina do perfl do usuario
    url(r'^sair/$', 'django.contrib.auth.views.logout',{'next_page':'index'},name='logout'), #usado para deslogar
    url(r'^central/perfil/editar/$', views.editar,name = "editar"),
    url(r'^central/perfil/senha/$', views.trocarsenha,name = "trocarsenha"),
]
