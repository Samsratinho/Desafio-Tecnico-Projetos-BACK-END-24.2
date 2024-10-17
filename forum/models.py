from django.db import models


class Comentario(models.Model):
    titulo = models.CharField(
        max_length=100, unique=True, null=False, blank=False
    )
    conteudo = models.TextField(null=False, blank=False)
    autor = models.CharField(max_length=50, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.titulo
