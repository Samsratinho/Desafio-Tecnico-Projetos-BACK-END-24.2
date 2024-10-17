from django.db import models


class CategoriaVideos(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False)
    descricao = models.CharField(max_length=100, unique=True, null=True)
    imagem = models.ImageField(upload_to='descricao/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Material(models.Model):
    categoria = models.ForeignKey(CategoriaVideos, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, unique=False, null=False)
    imagem = models.ImageField(upload_to='material/', blank=True, null=True)

    def __str__(self):
        return self.titulo