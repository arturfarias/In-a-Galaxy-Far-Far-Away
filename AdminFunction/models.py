from django.db import models

class CadastroLab(models.Model):
    laboratorio = models.CharField(max_length=50,)

    def __unicode__(self):
        return self.laboratorio
