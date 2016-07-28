from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.index,name = "index"),
    url(r'^central/$', views.central),
    url(r'^central/registro/$', views.registro),
    url(r'^central/perfil/$', views.perfil),

]
