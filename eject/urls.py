from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from home.views import ahome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pais_e_profs/', include('pais_e_profs.urls')),
    path("", ahome),
    path('forum/', include('forum.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
