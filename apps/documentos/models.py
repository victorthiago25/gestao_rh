from django.db import models
from apps.funcionarios.models import funcionario

class documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(funcionario, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.descricao
