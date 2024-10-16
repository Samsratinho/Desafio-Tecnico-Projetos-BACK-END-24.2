from django.db import models


class CategoriaVideo(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.nome


class Material(models.Model):
    categoria = models.ForeignKey(CategoriaVideo, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, unique=True, null=False)
    imagem = models.ImageField(upload_to='material/')

    def __str__(self):
        return self.titulo
