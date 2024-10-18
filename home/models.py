from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True) # Nome da categoria.

    def __str__(self):
        return self.nome #Retorna o nome da categoria para melhor visualização
    
class card_Ferramentas(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    secondTitle = models.CharField(max_length=100, null=False, blank=False, default='Título secundário')
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="material/")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.secondTitle}" #Retorna os títulos concatenados para melhor visualização.