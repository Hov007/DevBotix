from django.contrib import admin
from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include("main.urls")),
    prefix_default_language=False
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)