from django.urls import path

from . import views


app_name = 'pais_e_profs'
urlpatterns = [
    path('', views.CategoriaMaterial.as_view(), name='pais_e_profs'),
]
