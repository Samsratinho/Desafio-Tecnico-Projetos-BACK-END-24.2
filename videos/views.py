from django.views import generic

from .models import CategoriaVideo


class Categoria_Videos(generic.ListView):
    model = CategoriaVideo
    template_name = 'videos.html'
    context_object_name = 'categoriasVideos'

    def get_queryset(self):
        return CategoriaVideo.objects.all()[:3]