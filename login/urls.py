from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.index,name = "index"),#Pagina index onde se localiza o login
    url(r'^central/$', views.central), #Pagina central do aplicativo
    url(r'^central/registro/$', views.registro), #Pagina de registro de usuario
    url(r'^central/perfil/$', views.perfil), #Pagina do perfl do usuario
    url(r'^sair/$', 'django.contrib.auth.views.logout',{'next_page':'index'},name='logout'), #usado para deslogar 

]
