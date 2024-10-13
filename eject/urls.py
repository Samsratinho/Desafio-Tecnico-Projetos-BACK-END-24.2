from django.contrib import admin
from django.urls import path
from eject_app.views import ahome

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ahome),
]
