from django.shortcuts import render

from .models import Categoria


def listar_materiais(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'pais_e_profs/pais_e_profs.html',
        context={'categorias': categorias},
    )
