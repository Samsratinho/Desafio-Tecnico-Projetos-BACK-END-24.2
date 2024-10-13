from django.contrib import admin
from django.urls import path
from eject_app.views import ahome

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ahome),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
