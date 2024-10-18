from django.views import generic

from .models import CategoriaVideos, Material


class Categoria_Videos(generic.ListView):
    model = CategoriaVideos
    template_name = 'videos/videos.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        return CategoriaVideos.objects.all()
