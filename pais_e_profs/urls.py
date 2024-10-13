from django.urls import path

from . import views


app_name = 'pais_e_profs'
urlpatterns = [
    path('', views.listar_materiais, name='pais_e_profs'),
]
