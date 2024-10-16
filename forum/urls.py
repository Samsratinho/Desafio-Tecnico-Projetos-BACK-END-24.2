from django.urls import path

from . import views


app_name = 'forum'
urlpatterns = [
    path('', views.mostrar_comentarios, name='forum'),
    path('post/', views.salvar_comentario, name='salvar_comentario'),
]
