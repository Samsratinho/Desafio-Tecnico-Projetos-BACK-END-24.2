from django.shortcuts import render

from .models import Comentario


def mostrar_comentarios(request):
    comentarios = Comentario.objects.all().order_by('-data_criacao')
    return render(request, 'forum/forum.html', {'comentarios': comentarios})
