from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns(
    'website.views', url(r'^$', 'index'), url(r'^movies/$', 'movies'),
    url(r'^proj/$', 'projections'), url(r'^reserv/$', 'reservations'),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
