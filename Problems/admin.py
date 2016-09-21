from django.contrib import admin
from .models import Problema, Equipamento,Lab,Tipo_de_equipamento

admin.site.register(Lab)
admin.site.register(Tipo_de_equipamento)
admin.site.register(Problema)
admin.site.register(Equipamento)
