from django.db import models


class home(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="")
