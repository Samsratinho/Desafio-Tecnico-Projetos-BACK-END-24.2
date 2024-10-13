from django.shortcuts import render
from .models import home


def ahome(request):
    pageHome = home.objects.all()
    return render(request, "eject_app/home.html", {"pageHome": home})
