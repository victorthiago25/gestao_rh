from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import departamento
from apps.empresa.models import Empresa

class funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome