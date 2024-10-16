from django.views import generic

from .models import Categoria


class CategoriaMaterial(generic.ListView):
    model = Categoria
    template_name = 'pais_e_profs/pais_e_profs.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        return Categoria.objects.all()[:3]
