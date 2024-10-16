from django.shortcuts import render
from .models import card_Ferramentas


def ahome(request):
    # Aqui eu to chamando todos os objetos da classe card_Ferramentas e armazenando na variável pageHome.
    videos= card_Ferramentas.objects.filter(categoria_id = 1)
    atividades= card_Ferramentas.objects.filter(categoria_id = 2)
    jogos= card_Ferramentas.objects.filter(categoria_id = 3)
    # Agora estou enviando os dados carregados para o template.
    return render(request, "eject_app/home.html",{
        "videos": videos,
        "atividades": atividades,
        "jogos": jogos
    })
