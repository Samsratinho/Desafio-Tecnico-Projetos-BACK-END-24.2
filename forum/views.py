from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Comentario


def mostrar_comentarios(request):
    comentarios = Comentario.objects.all().order_by('-data_criacao')
    return render(request, 'forum/forum.html', {'comentarios': comentarios})


def salvar_comentario(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        conteudo = request.POST['caixadetexto']
        novo_comentario = Comentario(
            titulo=titulo,
            autor='Cavalo anônimo',
            conteudo=conteudo,
        )
        novo_comentario.save()
        return HttpResponseRedirect(reverse('forum:forum'))

    return HttpResponseRedirect(reverse('forum:forum'))
