from django.urls import path

from . import views


app_name = 'videos'
urlpatterns = [
    path('', views.Categoria_Videos.as_view(), name='videos'),
]