from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^central/itens/$', views.cadastro_itens,name = "itens"),
    url(r'^central/problemas/$', views.problemas,name = "problemas"),
    url(r'^central/lista/$', views.lista,name = "lista"),
    url(r'^central/lista/(?P<pk>[0-9]+)/$', views.list_detail,name = "list_detail"),
    url(r'^central/lista/(?P<pk>[0-9]+)/edit/$', views.list_edit, name='list_edit'),
]
