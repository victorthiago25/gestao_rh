from django.db import models

class registro_hora_extra(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.motivo
